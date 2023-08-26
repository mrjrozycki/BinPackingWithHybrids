import base.instance as Instance
import base.bin as Bin

class Base():

    def __init__(self):
        self.inst = Instance.Instance()
        self.bins = []

    def load_instance(self, filename):
        self.inst.read_file(filename)
        self.inst.load_instance()

    def sort_items(self):
        self.inst.items.sort(key=lambda x: x.get_size(0), reverse=True)

    def put_item(self, item, bin):
        if bin.item_fit(item):
            bin.add_item(item)
            return True
        return False
    
    def add_bin(self):
        bin = Bin.Bin(len(self.bins), self.inst.get_bin_cap().copy())
        self.bins.append(bin)
        return bin
    
    def calculate_lower_bound(self):
        return self.inst.calculate_lower_bound()