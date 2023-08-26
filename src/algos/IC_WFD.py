import numpy as np

import base.base as Base


class WFD(Base.Base):

    def __init__(self):
        super().__init__()

    def count_space_left(self, bin, item):
        difference = []
        for i in range(len(bin.get_capacity())):
            difference.append(bin.get_capacity()[i] - item.get_sizes()[i])
        return max(difference)


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
            if max_bin is None:
                max_bin = self.add_bin()
            self.put_item(item, max_bin)


