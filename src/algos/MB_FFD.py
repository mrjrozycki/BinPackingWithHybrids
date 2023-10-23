import base.base as Base
import sys

class MB_FFD(Base.Base):

    def __init__(self, n_bins=0):
        super().__init__(n_bins)


    def run(self):
        self.create_copies()
        self.calibrate_LB_and_n_bins()
        for b in range(self.LB, self.n_bins):
            self.maybe_copy_bins()
            self.copy_and_sort_items()
            self.put_away_too_big_items()
            print(self.inst.items[0].get_sizes())
            [self.add_bin() for _ in range(b-len(self.bins))]

            while self.inst.items:
                item = self.inst.items.pop(0)
                for bin in self.bins:
                    if self.put_item(item, bin):
                        break
                else:
                    self.inst.items.append(item)
                    break

            if not self.inst.items and not self.items_too_big:
                return True
            elif b+1 == self.n_bins and self.inst.items and self.stage == None:
                raise Exception("No bin found for item, to few bins.")
            elif b+1 == self.n_bins and self.inst.items and self.stage == 1:
                return False
            elif b+1 == self.n_bins and self.items_too_big and self.stage == 1:
                self.return_too_big_items()
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
            

