class cat:
	def __init__(self):
		# Atrributes
		self.name = ""
		self.age = 0
		self.food_brain = {}
		
	# Functions
	def set_name(self, new_name):
		self.name = new_name

	def cry(self):
		print('Meow')

	def eat(self, food_name, food_taste):
		self.food_brain[food_name] = food_taste
		self.age += 1

	def eat_many_foods(self, food_lst, taste_lst):
		for i in range(len(food_lst)):
			self.food_brain[food_lst[i]] = taste_lst[i]
			self.age += 1


mycat = cat()
mycat.set_name('Coco')
print('name of mycat: %s' % mycat.name)
print('age of mycat: %d' % mycat.age)
mycat.eat('Mango', 'Good')
print('age of mycat: %d' % mycat.age)
print('foods mycat had:', mycat.food_brain)
mycat.eat_many_foods(['Apple', 'Strawberry'], ['Amazing', 'Great'])
print(mycat.food_brain)

'''
# readline()
with open('./coco.txt', 'r') as f:
	while True:
		line = f.readline()
		print(line)
		if line == "":
			break

# readlines()
with open('./coco.txt', 'r') as f:
	lines = f.readlines()

print(lines)
# print('an' in 'can')
'''
