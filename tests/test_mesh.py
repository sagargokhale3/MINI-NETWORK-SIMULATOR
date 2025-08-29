from topology import Topology
from host import Host

def test_mesh():
    topo = Topology().build_mesh(n=4)
    h1 = Host("H1")
    h2 = Host("H2")
    packet = h1.send_packet("H2", "Testing Mesh Topology")
    h2.receive_packet(packet)

if __name__ == "__main__":
    test_mesh()