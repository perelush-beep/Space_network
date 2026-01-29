from satellite import *
from space_network_lib import *

earth = Earth("earth", 0)
sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)
sat3 = Satellite("sat3", 300)
sat4 = Satellite("sat4", 400)
p1 = Packet("can you hear me major Tom?", sat1, sat2)
p_final = Packet("Hello from earth", sat3, sat4)
p_sat2_to_sat3 = RelayPacket(p_final, sat2, sat3)
p_sat1_to_sat2 = RelayPacket(p_sat2_to_sat3, sat1, sat2)
p_earth_to_sat1 = RelayPacket(p_sat1_to_sat2, earth, sat1)

try:
    attempt_transmission(p_earth_to_sat1)
except BrokenConnectionError:
    print("Transmission failed")

