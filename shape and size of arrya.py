import numpy as np
np.random.seed(0)
x1=np.random.randint(10, size=6) #create id array
x2=np.random.randint(10, size=(3,4)) #create 2d array
x3=np.random.randint(10, size=(3,4,5)) #multidimension array
print(x3.dim) #3
print(x3.shape)
print(x3.size)
