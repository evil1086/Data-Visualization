#Bar chart

from matplotlib import pyplot as plt
from matplotlib import style
plt.bar([1,3,5,7,9],[5,2,7,8,2],label='Example_one',color='c')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='Example_two',color='g')
plt.legend()
plt.xlabel('Bar_number')
plt.ylabel('Bar_height')
plt.title('Bar_Graph')
plt.grid(True,'K')
plt.show()