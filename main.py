from satellite import *
from space_network_lib import *

earth = Earth("earth", 0)
sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)
p1 = Packet("can you hear me major Tom?", sat1, sat2)
p_final = Packet("Hello from earth", sat1, sat2)
p_earth_to_sat1 = RelayPacket(p_final, earth, sat1)

try:
    attempt_transmission(p_earth_to_sat1)
except BrokenConnectionError:
    print("Transmission failed")

