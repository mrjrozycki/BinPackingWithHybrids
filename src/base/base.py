import numpy as np

import base.instance as Instance
import base.bin as Bin

class Base():

    def __init__(self, n_bins=0):
        self.inst = Instance.Instance()
        self.bins = []
        self.stage = None
        if n_bins is not np.inf:
            self.n_bins = int(n_bins)+1
        else:
            self.n_bins = n_bins

    def load_instance(self, filename):
        self.inst.read_file(filename)
        self.inst.load_instance()
        self.LB = self.inst.lower_bound

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
    
    def count_space_left(self, bin, item):
        difference = []
        for i in range(len(bin.get_capacity())):
            difference.append(bin.get_capacity()[i] - item.get_sizes()[i])
        return min(difference)
    
    def create_copies(self):
        self.items_copy = self.inst.items.copy()
        self.bins_copy = self.bins.copy()

    def calibrate_LB_and_n_bins(self):
        if self.n_bins <= self.LB:
            self.LB = self.n_bins
            self.n_bins+=1

    def maybe_copy_bins(self):
        if self.stage == 2:
            self.bins = self.bins_copy.copy()
        else:
            self.bins = []

    def copy_and_sort_items(self):
        self.inst.items = self.items_copy.copy()
        self.sort_items()

    def put_away_too_big_items(self):
        self.items_too_big = []
        for item in self.inst.items.copy():
            # check all dimensions
            for i in range(self.inst.dim):
                if item.sizes[i] > self.inst.cap[i]:
                    self.items_too_big.append(item)
                    self.inst.items.remove(item)
                    break


    def return_too_big_items(self):
        for item in self.items_too_big:
            self.inst.items.append(item)