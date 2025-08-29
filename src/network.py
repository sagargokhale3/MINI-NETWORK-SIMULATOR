from topology import Topology
from host import Host

if __name__ == "__main__":
    print("=== Mini Network Simulator ===")

    # Example: Build star topology
    topo = Topology().build_star(n_hosts=3)

    # Hosts
    host1 = Host("H1")
    host2 = Host("H2")

    # Send and receive packet
    packet = host1.send_packet("H2", "Hello from H1 to H2")
    host2.receive_packet(packet)

    print("Simulation finished ✅")