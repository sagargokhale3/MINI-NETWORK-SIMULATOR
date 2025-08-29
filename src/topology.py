from router import Router
from host import Host

class Topology:
    def __init__(self, type="star"):
        self.type = type
        self.routers = []
        self.hosts = []

    def build_star(self, n_hosts=3):
        center = Router("R0")
        self.routers.append(center)
        for i in range(n_hosts):
            host = Host(f"H{i}")
            router = Router(f"R{i+1}")
            center.add_link(router)
            router.add_link(center)
            self.routers.append(router)
            self.hosts.append(host)
        return self

    def build_ring(self, n=3):
        routers = [Router(f"R{i}") for i in range(n)]
        for i in range(n):
            routers[i].add_link(routers[(i+1) % n])
            routers[(i+1) % n].add_link(routers[i])
        self.routers.extend(routers)
        return self

    def build_mesh(self, n=3):
        routers = [Router(f"R{i}") for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                routers[i].add_link(routers[j])
                routers[j].add_link(routers[i])
        self.routers.extend(routers)
        return self