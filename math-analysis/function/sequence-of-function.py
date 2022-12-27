# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def PointwiseConvergeOfsequenceContinuousFunction():
    # 點態收斂無法保證連續函數收斂為連續函數
    xs = np.arange(-1, 1, 0.001)
    ns = range(1, 100)

    for n in ns:
        xs2n = xs**(2*n)
        ys = xs2n/(1+xs2n)
        plt.plot(xs, ys)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    PointwiseConvergeOfsequenceContinuousFunction()
