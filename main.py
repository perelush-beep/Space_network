from satellite import *
from space_network_lib import *


sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)
p1 = Packet("can you hear me major Tom?", sat1, sat2)
attempt_transmission(p1,2)