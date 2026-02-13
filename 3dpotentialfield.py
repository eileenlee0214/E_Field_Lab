import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
import tkinter as tk
from tkinter import filedialog
import os
os.environ['PATH'] = '/Library/TeX/texbin:/usr/local/bin:' + os.environ['PATH']

# latex
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

# open file dialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(title="Select CSV file",
                                       filetypes=[("CSV files", "*.csv")])
data = pd.read_csv(file_path, header=None)
voltage_data = data.values

# x axis: A-L (0-11)
# y axis: 1-10 (0-9)

rows, cols = voltage_data.shape

x_m = np.arange(cols) * 0.02
y_m = np.arange(rows) * 0.02
X, Y = np.meshgrid(x_m, y_m)

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# surface plot
surf = ax.plot_surface(X, Y, voltage_data,
                       cmap='coolwarm',
                       edgecolor='none',
                       alpha=0.9)

# labels / title
ax.set_xlabel(r'$x$ ($\times 10^{-2}$ m)', fontsize=12, fontweight='bold')
ax.set_ylabel(r'$y$ ($\times 10^{-2}$ m)', fontsize=12, fontweight='bold')
ax.set_zlabel(r'Voltage (V)', fontsize=12, fontweight='bold')
ax.set_title(r'\textbf{3D Electric Potential Field Map}', fontsize=14, fontweight='bold')

# tick marks
x_ticks = np.arange(0, cols * 2 + 1, 2)
y_ticks = np.arange(0, rows * 2 + 1, 2)
ax.set_xticks(x_ticks * 0.01)
ax.set_xticklabels([f'{int(tick)}' for tick in x_ticks])
ax.set_yticks(y_ticks * 0.01)
ax.set_yticklabels([f'{int(tick)}' for tick in y_ticks])

# colorbar
cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('Voltage (V)', fontsize=12)

# view : make it rotatable
ax.view_init(elev=30, azim=45)

plt.savefig("3dpotentialfield.png", dpi=300)
plt.show()
