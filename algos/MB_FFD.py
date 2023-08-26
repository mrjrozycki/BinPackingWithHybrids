import algos.base as Base


class MB_FFD(Base.Base):

    def __init__(self, n_bins=0, LOWER_BOUND=0):
        super().__init__()
        self.n_bins = int(n_bins)+1
        if LOWER_BOUND == 0:
            self.LB = self.calculate_lower_bound()
        else:
            self.LB = int(LOWER_BOUND)

    def run(self):
        items_copy = self.inst.items.copy()
        for b in range(self.LB, self.n_bins):
            self.bins = []
            self.inst.items = items_copy.copy()
            self.sort_items()
            for _ in range(b):
                self.add_bin()
            while len(self.inst.items) > 0:
                item = self.inst.items.pop(0)
                for bin in self.bins:
                    if self.put_item(item, bin):
                        break
                else:
                    break
            if len(self.inst.items) == 0:
                return
            elif b+1 == self.n_bins and self.inst.items:
                raise Exception("No bin found for item, to few bins.")







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
            

