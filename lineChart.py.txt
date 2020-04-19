#Line chart

from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
x = [1,2,3]
y = [4,5,1]
x1 = [2,3,4]
y1 = [5,6,2]
plt.plot(x,y,'g',label ='Line_One', linewidth = 5)
plt.plot(x1,y1,'c',label = 'Second_line', linewidth = 5)
plt.title('Test')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.grid(True,'K')
plt.show()