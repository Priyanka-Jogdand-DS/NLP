# import packages
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')

# data points as vectors
a = [0, 16000]
b = [0, 14000]

# lambda function 
func = lambda x: (7/8)*x

# 100 area data points
area = np.linspace(0,16200,100)
# 100 price data points
price = func(area)
# scatter plot of Price vs Area
plt.scatter(a, b, marker='o', color='purple')
# draw vector arrow 
plt.arrow(8000, 7000, 200, func(8200)-func(8000), shape='full', lw=0, length_includes_head=True, head_width=500, color='black')
# draw straight line
plt.plot(area, price, color='yellow')
# annotate data points 'a' and 'b'
for x, y in zip(a, b):
    plt.annotate('({}, {})'.format(x, y), xy=[x,y])
# label axes
plt.xlabel('Area of house')
plt.ylabel('Price of house')
# display plot
plt.show()