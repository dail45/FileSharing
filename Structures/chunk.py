class Chunk:
    def __init__(self, index=-1, compressType=None, data=b"",
                 hash=None):
        self.index = index
        self.compressType = compressType
        self.data = data
        self.hash = hash
