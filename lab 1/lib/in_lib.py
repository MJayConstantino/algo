import sys


class In:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.data = self.file.read().split()
        self.index = 0

    def read_int(self):
        value = int(self.data[self.index])
        self.index += 1
        return value

    def is_empty(self):
        return self.index >= len(self.data)

    def close(self):
        self.file.close()
