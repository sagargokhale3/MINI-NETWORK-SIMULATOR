from packet import Packet

class Host:
    def __init__(self, name):
        self.name = name

    def send_packet(self, dest, data):
        return Packet(self.name, dest, data)

    def receive_packet(self, packet):
        print(f"[{self.name}] received: {packet}")