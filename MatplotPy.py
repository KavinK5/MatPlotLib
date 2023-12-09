xAxis = [0,1,2,3,4,5,6,7,8,9,10]
yAxis = [0,1,4,7,9,13,17,20,23,26,30]

pyplot.plot(xAxis , yAxis , color='#ababab' , linewidth=2 , marker='*' , markersize=10 , markeredgecolor='#000' ,linestyle='-')

pyplot.title('2D PLot',fontdict={'fontname':'Comic Sans MS','fontsize':'14'})

fontDICT = {'fontname':'Comic Sans MS',
            'fontsize':'12'}

pyplot.xlabel('X',fontdict = fontDICT)
pyplot.ylabel('Y',fontdict = fontDICT)

pyplot.xticks([0,1,3,5,7,9,11])
pyplot.yticks([0,5,10,15,20,25,31])

pyplot.show()
