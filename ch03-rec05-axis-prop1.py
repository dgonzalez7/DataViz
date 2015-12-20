from pylab import *

x = [1,2,3,4]
y = [5,4,3,2]

figure("A bunch of plots")

# subplot(231)
plot(x, y, linewidth = 1.5, marker = 'o', ls = ':', c = 'g')

show()