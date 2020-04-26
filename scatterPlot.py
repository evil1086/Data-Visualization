#scatterPlot

import matplotlib.pyplot as plt
x= [1,2,3,4,5,6]
y= [7,8,9,10,11,12]
plt.scatter(x,y,label='Skitcat',color='c')
plt.title('Scattplot')
plt.xlabel('lenght')
plt.ylabel('height')
plt.legend()
plt.show()