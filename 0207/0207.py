import numpy as np

arr = np.loadtxt('./mat.txt', delimiter=',')
arr2 = np.matmul(arr, arr.T)

np.savetxt('./resultmat.tsv', arr2, delimiter='\t', fmt='%.3lf')
# import pandas as pd

# df = pd.read_csv('./sample.csv', sep=',', names=['이름', '나이', '키'])

# for n, a, h in zip(df['이름'], df['나이'], df['키']):
# 	print(n, a, h)

# names = ['철수', '영희', '영수']
# ages = [0, 13, 5]
# heights = [0, 160, 50]

# for n, a, h in zip(names, ages, heights):
# 	print(n, a, h)

# f = open('./sample.csv', 'r')
# lines = f.readlines()
# f.close()

# ns, ags, hs = [], [], []
# for line in lines:
# 	lst = line.split(',')
# 	ns.append(lst[0])
# 	ags.append(int(lst[1]))
# 	hs.append(int(lst[2]))

# print(ns)
# print(ags)
# print(hs)


# names = ['철수', '영희', '영수']
# ages = [0, 13, 5]
# heights = [0, 160, 50]

# # lst = [3, 2, 0]
# 검색어가 있고
# 검색이 되면 value 를 프린트 해주고
# 검색이 안되면 에러 메세지 프린트 해주자.


# # print(3 in lst)
# # print(3 not in lst)


# fruit_color_table = {}
# fruit_color_table = dict()

# # fruit_color_table['key'] = 'val'
# fruit_color_table['apple'] = 'red'
# fruit_color_table['orange'] = 'orange'
# fruit_color_table['mango'] = 'yellow'
# fruit_color_table['strawberry'] = 'red'

# print(fruit_color_table)
# print(fruit_color_table['apple'])
# print(fruit_color_table.keys())
# print(fruit_color_table.values())
# print('red' in fruit_color_table.values())

# lst = []
# lst = list()

# import numpy as np

# M_lst = [[3, 2, 0], [6, 2, 1], [-2, 1, 0]]
# M_arr = np.array([[3, 2, 0], [6, 2, 1], [-2, 1, 0]])

# print(M_lst[0:2][0])
# print(M_arr[0:1, 0])

# arr = np.array([1, 2, 3, 4])

# arr2 = np.array([1, 2, 3, 4])

# inner_product = arr.dot(arr2)



