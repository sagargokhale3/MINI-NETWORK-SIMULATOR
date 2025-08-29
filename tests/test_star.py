from topology import Topology
from host import Host

def test_star():
    topo = Topology().build_star(n_hosts=3)
    h1 = Host("H1")
    h2 = Host("H2")
    packet = h1.send_packet("H2", "Testing Star Topology")
    h2.receive_packet(packet)

if __name__ == "__main__":
    test_star()