import numpy as np

import base.base as Base


class BFD(Base.Base):

    def __init__(self):
        super().__init__()

    def count_space_left(self, bin, item):
        difference = []
        for i in range(len(bin.get_capacity())):
            difference.append(bin.get_capacity()[i] - item.get_sizes()[i])
        return min(difference)


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
            if min_bin is None:
                min_bin = self.add_bin()
            self.put_item(item, min_bin)


