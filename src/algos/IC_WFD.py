import numpy as np

import base.base as Base


class WFD(Base.Base):

    def __init__(self, n_bins=np.inf):
        super().__init__(n_bins)


    def run(self):
        self.sort_items()
        while self.inst.items:
            max_space = -1
            max_bin = None
            item = self.inst.items.pop(0)
            for bin in self.bins:
                if (self.count_space_left(bin, item) > max_space) and (self.count_space_left(bin, item) >= 0):
                    max_space = self.count_space_left(bin, item)
                    max_bin = bin
            if (max_bin is None) and (len(self.bins) < self.n_bins):
                max_bin = self.add_bin()
            elif max_bin is None and len(self.bins) == self.n_bins:
                self.inst.items.append(item)
                return False
            if not(self.put_item(item, max_bin)):
                self.inst.items.append(item)
                self.bins.remove(max_bin)
                return False
        return True


