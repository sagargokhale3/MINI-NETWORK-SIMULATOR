class Packet:
    def __init__(self, src, dest, data):
        self.src = src
        self.dest = dest
        self.data = data

    def __str__(self):
        return f"Packet(src={self.src}, dest={self.dest}, data={self.data})"