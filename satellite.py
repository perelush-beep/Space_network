import time
from abc import ABC
from sys import exception

from space_network_lib import SpaceEntity, Packet, TemporalInterferenceError, DataCorruptedError, SpaceNetwork, \
    LinkTerminatedError, OutOfRangeError


class Satellite(SpaceEntity):
#Level_1
    def __init__(self, name:str, distance_from_earth:float):
        super().__init__(name, distance_from_earth)

    def receive_signal(self, packet: Packet):
        print(f"Name: {self.name}, Received: {packet}")

class BrokenConnectionError(Exception):
    pass
def attempt_transmission(packet: Packet, level):
    net = SpaceNetwork(level=level)
    while True:
        try:
            net.send(packet)
            return
        except TemporalInterferenceError:
            print("interference waiting...")
            time.sleep(2)
        except DataCorruptedError:
            print("data corrupted, retrying...")
        except LinkTerminatedError:
            print("link lost")
            raise BrokenConnectionError()
        except OutOfRangeError:
            print("target out of range")
            raise BrokenConnectionError()





