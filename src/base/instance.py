import sys
import math
import base.item as Item

class Instance():

    def __init__(self):
        self.lines = []
        self.items = []
        self.dim = -1
        self.cap = []
        self.lower_bound = None

    def read_file(self, filename):
        f = open(filename, 'r')
        self.lines = f.readlines()
        f.close()

    def load_instance(self):
        self.set_dim()
        self.set_bin_cap()
        self.set_items()
        self.set_lower_bound()
    
    def set_dim(self):
        self.dim = int(self.lines[0])
    
    def set_bin_cap(self):
        self.cap = self.lines[1].strip().split(" ")
        self.cap = [int(i) for i in self.cap]
    
    def set_items(self):
        self.lines.pop(0)
        self.lines.pop(0)
        self.lines.pop(0)
        for index, line in enumerate(self.lines):
            line = line.strip()
            line = line.split(' ')
            sizes = []
            for i in line[:-1]:
                sizes.append(int(i))
            self.items.append(Item.Item(index, sizes))

    def get_dim(self):
        return self.dim
    
    def get_bin_cap(self):
        return self.cap
    
    def get_items(self):
        sizes = []
        for i in self.items:
            sizes.append(i.get_sizes())
        return sizes
    
    #Lower bound is calculated as the sum of all the items divided by the bin capacity
    def calculate_lower_bound(self):
        max_n_bins = 0
        for dim in range(self.dim):
            total = 0
            for item in self.items:
                total += item.get_size(dim)
            if math.ceil(total/self.cap[dim]) > max_n_bins:
                max_n_bins = math.ceil(total/self.cap[dim])
        return max_n_bins
    
    def set_lower_bound(self):
        self.lower_bound = self.calculate_lower_bound()


if __name__ == '__main__':
    inst = Instance()
    inst.read_file(sys.argv[1])
    inst.load_instance()
    # print(inst.get_dim())
    # print(inst.get_bin_cap())
    # print(inst.get_items())
    print(inst.calculate_lower_bound())

