import matplotlib
from matplotlib import pyplot
import numpy

pyplot.resize(figsize = (6 , 4) , dip = 200) #for length and width of the graph
#Include this immediately after the importing code line

x1 = numpy.arange(1,11,2)
y2 = numpy.arange(2,12,2)

pyplot.plot(x1 , y1 , label = "1x")

pyplot.legend() #Code for the legend to be shown
pyplot.show()
