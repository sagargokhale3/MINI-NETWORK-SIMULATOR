from topology import Topology
from host import Host

def test_ring():
    topo = Topology().build_ring(n=4)
    h1 = Host("H1")
    h2 = Host("H2")
    packet = h1.send_packet("H2", "Testing Ring Topology")
    h2.receive_packet(packet)

if __name__ == "__main__":
    test_ring()