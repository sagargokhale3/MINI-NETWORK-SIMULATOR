import heapq

class Router:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}  # neighbor: weight

    def add_link(self, neighbor, weight=1):
        self.neighbors[neighbor] = weight

    def shortest_path(self, dest):
        distances = {self: 0}
        prev_nodes = {}
        pq = [(0, self)]

        while pq:
            dist, node = heapq.heappop(pq)
            if node == dest:
                break
            for neighbor, weight in node.neighbors.items():
                new_dist = dist + weight
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    prev_nodes[neighbor] = node
                    heapq.heappush(pq, (new_dist, neighbor))

        path, current = [], dest
        while current in prev_nodes:
            path.insert(0, current)
            current = prev_nodes[current]
        if path:
            path.insert(0, self)
        return path

    def __repr__(self):
        return f"Router({self.name})"