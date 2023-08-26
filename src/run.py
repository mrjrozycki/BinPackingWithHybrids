import sys

import algos.IC_FFD as FFD
import algos.IC_BFD as BFD
import algos.IC_WFD as WFD
import algos.BC as BC
import algos.MB_FFD as MB_FFD
import algos.MB_BFD as MB_BFD
import algos.MB_WFD as MB_WFD
import algos.Thr_bin_num as Thr_bin_num

def pick_algo(name):
    if name == "FFD":
        algo = FFD.FFD()
    elif name == "MB_FFD":
        algo = MB_FFD.MB_FFD(sys.argv[3])
    elif name == "BFD":
        algo = BFD.BFD()
    elif name == "MB_BFD":
        algo = MB_BFD.MB_BFD(sys.argv[3])
    elif name == "WFD":
        algo = WFD.WFD()
    elif name == "MB_WFD":
        algo = MB_WFD.MB_WFD(sys.argv[3])
    elif name == "BC":
        algo = BC.BinCentric()
    elif name == "THR_1":
        algo = Thr_bin_num.bin_number(algo1=pick_algo(sys.argv[3]), algo2=pick_algo(sys.argv[4]))
    else:
        raise ValueError("Invalid algorithm name")
    return algo


if __name__ == "__main__":
    algo = pick_algo(sys.argv[1])
    algo.load_instance(sys.argv[2])
    algo.run()
    print(f"Numbers of bins: {len(algo.bins)}")
    for bin in algo.bins:
        print(f"""ID: {bin.id}, Capacity left : {bin.get_capacity()}, Items: {bin.get_items()}, Items sizes: {bin.get_items_sizes()}""", end="\n")