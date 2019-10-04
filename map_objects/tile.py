class Tile: #Map tile object
    def __init__(self, blocked, block_sight=None): #None ~= Null value in other languages
        self.blocked=blocked
        if block_sight is None:
            block_sight=blocked

        self.block_sight=block_sight
