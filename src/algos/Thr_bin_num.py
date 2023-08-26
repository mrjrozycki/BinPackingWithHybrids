import numpy as np
import sys
import base.base as Base

class bin_number(Base.Base):

    def __init__(self, n_bins=0, algo1=None, algo2=None, param=1):
        super().__init__(n_bins)
        self.algo1 = algo1
        self.algo2 = algo2
        self.param = param
        self.algo1.n_bins = None


    def run(self):
        self.algo1.load_instance(sys.argv[2])
        self.algo1.n_bins = self.algo1.inst.lower_bound*self.param
        if not (self.algo1.run()):
            print(f"Looking for solution failed. Number of filled bins: {len(self.algo1.bins)}")

        self.algo2.load_instance(sys.argv[2])
        self.algo2.bins = self.algo1.bins.copy()
        self.algo2.inst.items = self.algo1.inst.items.copy()
        self.algo2.run()
        self.bins = self.algo2.bins.copy()