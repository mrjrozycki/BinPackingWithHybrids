import numpy as np

import algos.base as Base


class BinCentric(Base.Base):

    def __init__(self):
        super().__init__()

    def count_space_left(self, bin, item):
        difference = []
        for i in range(len(bin.get_capacity())):
            difference.append(bin.get_capacity()[i] - item.get_sizes()[i])
        return min(difference)
    
    def check_if_any_item_fits(self, items, bin):
        for item in items:
            if bin.item_fit(item):
                return True
        return False

    def run(self):
        self.sort_items()
        while True:
            bin = self.add_bin()
            while self.check_if_any_item_fits(self.inst.items, bin):
                best_item = None
                best_space = np.inf
                for item in self.inst.items:
                    if self.count_space_left(bin, item) < best_space and self.count_space_left(bin, item) >= 0:
                        best_space = self.count_space_left(bin, item)
                        best_item = item
                self.inst.items.remove(best_item)
                self.put_item(best_item, bin)
            if not self.inst.items:
                break


