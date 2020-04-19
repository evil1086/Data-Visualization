#Pie Chart
#If your data set is in the negative state then dont prefer this chart
import matplotlib.pyplot as plt
slices = [7,2,11,13]
sleeping = [2,4,6,8,9]
eating = [3,6,8,4,3]
working = [2,6,4,7,9]
playing = [3,6,8,6,3]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['c','m','r','b']
plt.pie(slices,
        labels=activities,
        colors=colors,
        startangle=180,
        shadow=True,
        explode=(0,0,0.1,0.1),
       autopct='%1.1f%%')
plt.show()