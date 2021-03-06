import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import pandas as pd
import math

# 3Dgraphを作成
class Ploter_3D():
    def __init__(self, x, y, z):
        self.x = x # 1次元可能
        self.y = y # 1次元可能
        self. z = z # 2次元配列でほしい
        # グラフ作成
        self.fig = plt.figure()
        self.axis = self.fig.add_subplot(111, projection='3d')
    
    def plot_3d(self):
        self.axis.set_xlabel('xlabel')
        self.axis.set_ylabel('ylabel')
        self.axis.set_zlabel('zlabel')

        X, Y = np.meshgrid(self.x, self.y)
        Z = self.z

        self.axis.plot_surface(X, Y, Z, cmap=cm.GnBu)

        plt.show()

def main():
    # 軸の作成
    x = np.array([i for i in range(50)]) # 1次元のデータ
    y = np.array([i for i in range(50)]) # 2次元のデータ
    z = np.random.rand(50, 50)
    ploter = Ploter_3D(x, y, z)
    ploter.plot_3d()
    
if __name__ == '__main__':
    main()