x = {'username' : 'Samuel', 'books' : ['里外更新', '杰出青少年的七个习惯', '万历十五年']}
from copy import deepcopy
y = deepcopy(x)
# y = x.copy()
y['username'] = 'Mercy'
print(y)
y['books'][0] = '少有人走的路'
print(x)


