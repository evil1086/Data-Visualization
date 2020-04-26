#stackPlot

import matplotlib.pyplot as plt
days = [1,2,3,4,5]
sleeping = [2,4,6,8,9]
eating = [3,6,8,4,3]
working = [2,6,4,7,9]
playing = [3,6,8,6,3]
plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='g',label='eating',linewidth=5)
plt.plot([],[],color='c',label='working',linewidth=5)
plt.plot([],[],color='r',label='playing',linewidth=5)
plt.stackplot(sleeping,eating,working,playing,colors=['m','g','c','k'])
plt.title('Stackplot')
plt.xlabel('lenght')
plt.ylabel('height')
plt.legend()
plt.show()
