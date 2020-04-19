# HistoGram

import matplotlib.pyplot as plt
population = [10,12,14,14,151,61,56,67,78,89,45,65,76,87,98,86]
distribution =[10,20,30,40,50,60,70,80,90,100]
plt.hist(population,distribution, histtype='bar',rwidth=0.8)
plt.title('Histogram')
#plt.legend()
plt.xlabel('Count')
plt.ylabel('height')
plt.show()