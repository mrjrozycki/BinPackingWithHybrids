import numpy as np

import base.base as Base


class MB_BFD(Base.Base):

    def __init__(self, n_bins=0):
        super().__init__(n_bins)
            

# Od chata
    def run(self):
        items_copy = self.inst.items.copy()
        for b in range(self.LB, self.n_bins):
            self.bins = []
            self.inst.items = items_copy.copy()
            self.sort_items()
            for _ in range(b):
                self.add_bin()
            while self.inst.items:
                min_space = np.inf
                min_bin = None
                item = self.inst.items.pop(0)
                for bin in self.bins:
                    if (self.count_space_left(bin, item) < min_space) and (self.count_space_left(bin, item) >= 0):
                        min_space = self.count_space_left(bin, item)
                        min_bin = bin
                if min_bin is None:
                    break
                self.put_item(item, min_bin)
            if len(self.inst.items) == 0:
                return
            if b+1 == self.n_bins and self.inst.items:
                raise Exception("No bin found for item, to few bins.")
            

    # def run(self):
    #     LB = self.calculate_lower_bound()
    #     items_copy = self.inst.items.copy()
    #     for b in range(LB, self.n_bins):
    #         self.bins = []
    #         self.inst.items = items_copy.copy()
    #         self.sort_items()
    #         for _ in range(b):
    #             self.add_bin()
    #         while self.inst.items:
    #             min_space = np.inf
    #             min_bin = None
    #             item = self.inst.items.pop(0)
    #             for bin in self.bins:
    #                 if (self.count_space_left(bin, item) < min_space) and (self.count_space_left(bin, item) >= 0):
    #                     min_space = self.count_space_left(bin, item)
    #                     min_bin = bin
    #                 #If there is no bin with enough space, check the next b bins
    #                 if min_bin is None:
    #                     break
    #             if min_bin is None:
    #                 break
    #             self.put_item(item, min_bin)
    #         if not self.inst.items:
    #             break
    #     if self.inst.items:
    #         raise Exception("No bin found for item, to few bins.")