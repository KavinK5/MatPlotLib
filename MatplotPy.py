import matplotlib
from matplotlib import pyplot
import numpy

pyplot.figure(figsize=(6,4),dpi=200)

xAxis = numpy.arange(1,20,2)
yAxis = numpy.arange(21,40,2)

x2Axis = [3,5.0,7.5,10,12.5,15,17.5]
y2Axis = [22,30,32.5,28,30,38,30]

pyplot.plot(xAxis , yAxis , color='#ababab' , linewidth=2 , marker='*', markersize=8 , markeredgecolor='#000' ,linestyle='-', label = '1st')

pyplot.plot(x2Axis[0:6] , y2Axis[0:6] , color = '#000' , marker = '.' , linestyle='--' , label = '2nd')
pyplot.plot(x2Axis[5:] , y2Axis[5:] , color = '#000' , marker = '.' , linestyle='-')

pyplot.title('2D PLot',fontdict={'fontname':'Comic Sans MS','fontsize':'16'})

fontDICT = {'fontname':'Comic Sans MS',
            'fontsize':'12'}

pyplot.xlabel('X',fontdict = fontDICT)
pyplot.ylabel('Y',fontdict = fontDICT)

pyplot.legend()

pyplot.show()
