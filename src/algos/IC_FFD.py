import numpy as np

import base.base as Base


class FFD(Base.Base):

    def __init__(self, n_bins=np.inf):
        super().__init__(n_bins)

    def run(self):
        self.sort_items()
        while self.inst.items:
            item = self.inst.items.pop(0)
            for bin in self.bins:
                if self.put_item(item, bin):
                    break
            else:
                if (len(self.bins) < self.n_bins):
                    bin = self.add_bin()
                elif len(self.bins) == self.n_bins:
                    self.inst.items.append(item)
                    return False
                self.put_item(item, bin)