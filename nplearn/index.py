import numpy as np

# arr=np.random.randint(1,100,10)
# print(arr.argsort()[-3:])  # 获得最大3个的index
# print(arr[arr.argsort()[-3:]])  # 根据index获取值

arr2=np.random.randint(1, 100, 12)
arr2=np.reshape(arr2, (2, 2, 3))
print(arr2[:,:,None,:].shape)  # (2,2,1,3)
print(np.expand_dims(arr2, axis=2).shape)  # (2,2,1,3)
print(np.reshape(arr2, (2, 2, 1, 3)).shape)  # (2,2,1,3)