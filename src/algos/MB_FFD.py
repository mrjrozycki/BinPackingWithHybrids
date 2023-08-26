import base.base as Base


class MB_FFD(Base.Base):

    def __init__(self, n_bins=0):
        super().__init__(n_bins)

    def run(self):
        items_copy = self.inst.items.copy()
        bins_copy = self.bins.copy()
        if self.n_bins <= self.LB:
            self.LB = self.n_bins
            self.n_bins+=1
        for b in range(self.LB, self.n_bins):
            if self.stage == 2:
                self.bins = bins_copy.copy()
            else:
                self.bins = []
            self.inst.items = items_copy.copy()
            self.sort_items()
            for _ in range(b-len(self.bins)):
                self.add_bin()
            while len(self.inst.items) > 0:
                item = self.inst.items.pop(0)
                for bin in self.bins:
                    if self.put_item(item, bin):
                        break
                else:
                    break
            if len(self.inst.items) == 0:
                return True
            elif b+1 == self.n_bins and self.inst.items and self.stage == None:
                raise Exception("No bin found for item, to few bins.")
            elif b+1 == self.n_bins and self.inst.items and self.stage == 1:
                return False







        # self.sort_items()
        # for b in range(self.n_bins):
        #     self.add_bin()
        # while self.inst.items:
        #     item = self.inst.items.pop(0)
        #     for bin in self.bins:
        #         if self.put_item(item, bin):
        #             break
        #     else:
        #         raise Exception("No bin found for item, to few bins.")
            

