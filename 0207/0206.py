class Stack:
	def __init__(self):
		self.stack = []
		

class list:
	def __init__(self):
		self.listitself = []

	def append(self, new_item):
		self.listitself = self.listitself + [new_item]


lst = []
lst = list()
lst.append(new_item)
d = dict()
d = {}

sum(lst)

from collections import OrderedDict

class Cat:
	# Initializer
	# __init__ 의 이름을 갖는 함수
	def __init__(self):
		# Attributes
		self.name = "untitled"
		self.age = 0
		self.food_dict = OrderedDict()

	# Functions
	def achieve_name(self, new_name):
		self.name = new_name

	def acquire_food(self, new_food, new_taste):
		self.food_dict[new_food] = new_taste
		self.age += 1

	def eat_many_food(self, food_lst, taste_lst):
		for food, taste in zip(food_lst, taste_lst):
			self.food_dict[food] = taste
			self.age += 1


kitty0 = Cat()
kitty0.achieve_name('Gourmat')
kitty0.acquire_food('Apple', 'Good')
kitty0.eat_many_food(['Milk', 'Fish', 'Chicken'], ['Great', 'Okay', 'Fine'])
print(kitty0.age)
print(kitty0.food_dict)

'''
def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n - 2) + fib(n - 1)
'''

'''
reservoir (dict)
	- key = n
	- val = fib(n)
'''

'''
dynamic_fib
	- input: n, 현재 reservoir
	- output: fib(n), 업데이트 된 reservoir
'''
'''
def dynamic_fib(n, reservoir):
	if n == 0 or n == 1:
		reservoir[n] = ???
		return 1, reservoir
	else:
		# fib(n-2) 가 reservoir 에 있는지 체크
		if (n - 2) in reservoir.keys():
			# 있으면 -> 쓰고
			fib_n_2 = reservoir[n - 2]
		else:
			# 없으면 -> 구한다음 쓴다
			fib_n_2, reservoir = dynamic_fib(n - 2, reservoir)

		# fib(n-1) 가 reservoir 에 있는지 체크
		# 있으면 -> 쓰고
		# 없으면 -> 구한다음 쓴다


reservoir = {}
fib_n, reservoir = dynamic_fib(n, reservoir)
'''
'''
import pandas as pd

add_w = sum(df.몸무게)

sum_of_weight = 0
for n, w, h in zip(df.이름, df.)
	sum_of_weight += w
print(sum_of_weight)

# df = pd.read_csv('.txt', )

# name = ['철수', '영희', '영수']
# age = [0, 5, 2]
# sex = ['여성', '여성', '남성']


for n, a, s in zip(name, age, sex):
	...

for idx in range(len(name)):
	n = name[idx]
	a = age[idx]
	s = sex[idx]
	...

# dict comprehension
d = {'a': 1, 'b': 2, 'c': 3}

lst = ['a', 'b', 'c']
d = {lst[th]: th + 1 for th in range(len(lst))}

print(d)

# list comprehension

lst = [0, 1, 2, 3, 4]

# method 1
lst = []
for i in range(5):
	lst.append(i)

print(lst)

# method 2: comprehension 사용
lst = [i for i in range(5)]

print(lst)
'''