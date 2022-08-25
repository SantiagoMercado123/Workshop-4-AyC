# imports the needed methods from numerical python and matplotlib library
from numpy import loadtxt
from matplotlib import pyplot as plt

""" imports the experimental data """

#AVERAGE CASE

# unpacks the input size, the number of comparisons, and the elapsed time
size, comps, etime = loadtxt("C:/Users/Santi Mercado/OneDrive/Escritorio/AyC2 2.0/AyC2/BestCase.txt").T

""" visualization """

# closes all files and enables interactive plotting
plt.close('all')
plt.ion()
# creates a figure and a set of axes
fig, ax = plt.subplots()

# computes scaling constants to improve presentation
c1 = (size).mean() / comps.mean()
c2 = (size).mean() / etime.mean()
# plots the expected (theoretical) time as a function of size
ax.loglog(size, size,    color='black', linestyle='--',
          label='linear')
# plots the elapsed time as a function of size
ax.loglog(size, c2 * etime, color='black',  linestyle='', marker='o',
          markersize=12, label='elapsed-time')
# plots the number of comparisons as a function of size
ax.loglog(size, c1 * comps, color='red',   linestyle='', marker='*',
          markersize=12, label='comparisons')
ax.set_xlabel('input size, N')
ax.set_ylabel('time, t')
ax.set_title('best case')
ax.legend()

# exports the figure in PNG with a resolution of 600 DPI
fig.savefig("best.png", dpi=600)