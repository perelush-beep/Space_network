from satellite import Satellite
from space_network_lib import *
from satellite import *

network = SpaceNetwork()
sat1 = Satellite("sat1",100)
sat2 = Satellite("sat2",200)
p1 = Packet("can you hear me major Tom?", sat1, sat2)
network.send(p1)