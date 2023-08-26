import numpy as np
import sys
import math
import base.base as Base

class bin_number(Base.Base):

    def __init__(self, n_bins=0, algo1=None, algo2=None, param=0.5):
        super().__init__(n_bins)
        self.algo1 = algo1
        self.algo2 = algo2
        self.param = param
        self.algo1.n_bins = None


    def run(self):
        self.algo1.load_instance(sys.argv[2])
        self.algo1.stage = 1
        self.algo1.n_bins = math.ceil(self.algo1.inst.lower_bound*self.param)
        if not (self.algo1.run()):
            print(f"Finding solution failed. Number of filled bins: {len(self.algo1.bins)}")
        else:
            print(f"Solution found. Number of filled bins: {len(self.algo1.bins)}")
            self.bins = self.algo1.bins.copy()
            return True
        self.algo2.load_instance(sys.argv[2])
        self.algo2.stage = 2
        self.algo2.bins = self.algo1.bins.copy()
        self.algo2.inst.items = self.algo1.inst.items.copy()
        self.algo2.n_bins = self.algo1.inst.lower_bound*2
        self.algo2.run()
        self.bins = self.algo2.bins.copy()

class bin_cap(Base.Base):

    def __init__(self, n_bins=0, algo1=None, algo2=None, param=0.5):
        super().__init__(n_bins)
        self.algo1 = algo1
        self.algo2 = algo2
        self.param = param
        self.algo1.n_bins = None


    def run(self):
        self.algo1.load_instance(sys.argv[2])
        self.algo1.stage = 1
        self.algo1.n_bins = math.ceil(self.algo1.inst.lower_bound)
        cap_copy = self.algo1.inst.cap.copy()
        cap_for_adding = np.array(self.algo1.inst.cap) - (np.array(self.algo1.inst.cap)*self.param)
        self.algo1.inst.cap = np.array(self.algo1.inst.cap)*self.param
        self.algo1.inst.cap = [math.ceil(x) for x in self.algo1.inst.cap]
        if not (self.algo1.run()):
            print(f"Finding solution failed. Number of filled bins: {len(self.algo1.bins)}")
            for bin in self.algo1.bins:
                print(f"""ID: {bin.id}, Capacity left : {bin.get_capacity()}, Items: {bin.get_items()}, Items sizes: {bin.get_items_sizes()}""", end="\n")
        else:
            print(f"Solution found. Number of filled bins: {len(self.algo1.bins)}")
            self.bins = self.algo1.bins.copy()
            return True
        self.algo2.load_instance(sys.argv[2])
        self.algo2.stage = 2
        self.algo2.bins = self.algo1.bins.copy()
        self.algo2.inst.items = self.algo1.inst.items.copy()
        self.algo2.inst.cap = cap_copy
        for bin in self.algo2.bins:
            bin.capacity = np.array(bin.capacity) + cap_for_adding
        self.algo2.n_bins = self.algo1.inst.lower_bound*2
        self.algo2.run()
        self.bins = self.algo2.bins.copy()