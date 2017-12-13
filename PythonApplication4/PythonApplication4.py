import numpy as np
import matplotlib.pyplot as plt
from math import radians

def main():
    x = np.arange(0, radians(1800))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()
