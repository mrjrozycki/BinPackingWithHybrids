class Item():
    def __init__(self, id, sizes):
        self.id = id
        self.sizes = sizes
    
    def get_id(self):
        return self.id
    
    def get_sizes(self):
        return self.sizes
    
    def get_size(self, index):
        return self.sizes[index]
    
if __name__ == '__main__':
    item = Item(1, [1, 2, 3])
    print(item.get_id())
    print(item.get_sizes())
    print(item.get_size(0))
    print(item.get_size(1))
    print(item.get_size(2))