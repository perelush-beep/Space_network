import time

from space_network_lib import SpaceEntity, Packet, TemporalInterferenceError, DataCorruptedError, SpaceNetwork, \
    LinkTerminatedError, OutOfRangeError

class BrokenConnectionError(Exception):
    pass

class Satellite(SpaceEntity):
    def __init__(self, name:str, distance_from_earth:float):
        super().__init__(name, distance_from_earth)

    def receive_signal(self, packet: Packet):
        if isinstance(packet, RelayPacket):
            inner_packet = packet.data
            print(f'Unwrapping and forwarding to {inner_packet.receiver}')
            attempt_transmission(inner_packet)
        else:
            print(f"Final destination reached: {packet.data}")

class Earth(SpaceEntity):
    def __init__(self, name, distance_from_earth):
        super().__init__( name, distance_from_earth)

class RelayPacket(Packet):
    def __init__(self, packet_to_relay, sender, proxy):
        super().__init__(packet_to_relay, sender, proxy)

    def __repr__(self):
        return f"RelayPacket (Relaying {self.data} to {self.receiver} from {self.sender})"

def attempt_transmission(packet: Packet|RelayPacket):
    net = SpaceNetwork(level=4)
    while True:
        try:
            net.send(packet)
            return
        except TemporalInterferenceError:
            print("interference waiting...")
            time.sleep(2)
        except DataCorruptedError:
            print("data corrupted, retrying...")
        except LinkTerminatedError as e:
            print("link lost",e)
            raise BrokenConnectionError()
        except OutOfRangeError:
            print("target out of range")
            raise BrokenConnectionError()








