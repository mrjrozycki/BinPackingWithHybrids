import sys

import algos.IC_FFD as FFD
import algos.IC_BFD as BFD
import algos.IC_WFD as WFD
import algos.BC as BC
import algos.MB_FFD as MB_FFD
import algos.MB_BFD as MB_BFD

if __name__ == "__main__":
    if sys.argv[1] == "FFD":
        algo = FFD.FFD()
    elif sys.argv[1] == "MB_FFD":
        algo = MB_FFD.MB_FFD(sys.argv[3])
    elif sys.argv[1] == "BFD":
        algo = BFD.BFD()
    elif sys.argv[1] == "MB_BFD":
        algo = MB_BFD.MB_BFD(sys.argv[3])
    elif sys.argv[1] == "WFD":
        algo = WFD.WFD()
    elif sys.argv[1] == "BC":
        algo = BC.BinCentric()
    else:
        raise ValueError("Invalid algorithm name")
    algo.load_instance(sys.argv[2])
    algo.run()
    print(len(algo.bins))
    # for bin in algo.bins:
    #     for items in bin.get_items():
    #         print(bin.id, items, end=" ")