import numpy as np

import base.base as Base


class BFD(Base.Base):

    def __init__(self, n_bins=np.inf):
        super().__init__(n_bins)


    def run(self):
        self.sort_items()
        while self.inst.items:
            min_space = np.inf
            min_bin = None
            item = self.inst.items.pop(0)
            for bin in self.bins:
                if (self.count_space_left(bin, item) < min_space) and (self.count_space_left(bin, item) >= 0):
                    min_space = self.count_space_left(bin, item)
                    min_bin = bin
            if (min_bin is None) and (len(self.bins) < self.n_bins):
                min_bin = self.add_bin()
            elif min_bin is None and len(self.bins) == self.n_bins:
                self.inst.items.append(item)
                return False
            self.put_item(item, min_bin)
        return True