import base.item as Item

class Bin():
    def __init__(self, id, capacity):
        self.id = id
        self.items = []
        self.capacity = capacity

    def get_id(self):
        return self.id
    
    def get_capacity(self):
        return self.capacity
    
    def get_items(self):
        for item in self.items:
            yield item.get_sizes()
    
    def item_fit(self, item):
        for i in range(len(item.get_sizes())):
            if item.get_size(i) > self.capacity[i]:
                return False
        return True
    
    def add_item(self, item):
        self.items.append(item)
        for i in range(len(item.get_sizes())):
            self.capacity[i] -= item.get_size(i)

if __name__ == '__main__':
    b1 = Bin(1, [1000, 200])
    print(b1.get_id())
    print(b1.get_capacity())
    print(b1.item_fit(Item.Item(1, [1000, 201])))
    print(b1.add_item(Item.Item(1, [1000, 199])))


