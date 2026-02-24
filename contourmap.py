import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
import tkinter as tk
from tkinter import filedialog
from scipy.interpolate import RectBivariateSpline
import os

# making MacTeX work on my Mac...
os.environ['PATH'] = '/Library/TeX/texbin:/usr/local/bin:' + os.environ['PATH']

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# file dialog for csv input
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Select CSV file",
                                       filetypes=[("CSV files", "*.csv")])

if not file_path:
    print("No file selected")
    exit()

# read csv
data = pd.read_csv(file_path, header=None)
voltage_data = data.values

L, H = voltage_data.shape

# grid points
x = np.arange(H)
y = np.arange(L)

# interpolation function
f = RectBivariateSpline(y, x, voltage_data, kx=3, ky=3)

# create fine grid for smooth contours
x_fine = np.linspace(0, H-1, H*5)
y_fine = np.linspace(0, L-1, L*5)
X_fine, Y_fine = np.meshgrid(x_fine, y_fine)

# interpolating voltage data
voltage_fine = f(y_fine, x_fine)

# electric field for quiver using original data
X, Y = np.meshgrid(x, y)
Ey, Ex = np.gradient(voltage_data)
Ex = -Ex
Ey = -Ey

fig, ax = plt.subplots(figsize=(12, 10))

# use fine grid for smooth contours
contourf = ax.contourf(X_fine, Y_fine, voltage_fine,
                       levels=30, cmap='viridis', alpha=0.7)

contour = ax.contour(X_fine, Y_fine, voltage_fine, levels=15, colors='white', 
                     linewidths=1.5, linestyles='solid')
ax.clabel(contour, inline=True, fontsize=8, fmt=r'%0.1f V', colors='white')

# colorbar
cbar = plt.colorbar(contourf, ax=ax)
cbar.set_label(r'Voltage (V)', rotation=270, labelpad=20)

# labels
ax.set_xlabel(r'x position from the bottom left corner (cm)')
ax.set_ylabel(r'y position from the bottom left corner (cm)')
ax.set_title(r'2D Equipotential Lines')
ax.set_aspect('equal')
ax.grid(True, alpha=0.3, color='white', linestyle='--')

plt.tight_layout()

plt.savefig("contourmap.png", dpi=300)
plt.show()