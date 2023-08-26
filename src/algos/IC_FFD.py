import base.base as Base


class FFD(Base.Base):

    def __init__(self):
        super().__init__()

    def run(self):
        self.sort_items()
        while self.inst.items:
            item = self.inst.items.pop(0)
            for bin in self.bins:
                if self.put_item(item, bin):
                    break
            else:
                bin = self.add_bin()
                self.put_item(item, bin)