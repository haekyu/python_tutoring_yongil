함수
    - 이름: ....
    - 인풋: 어떤 리스트
    - 중간: 'length = ??'
    - 아웃풋: 인풋 리스트의 길이


def g(x, y):
    a = x + y
    b = x * y
    c = x - y
    return a, b, c


result = g(3, 3)
print(result)
print(result[1])

r1, r2, r3 = g(3, 3)
print(r2)

'''
g(x, y) = x + y, x * y, x - y




def prt_element(lst):
    for e in lst:
        print(e)

# f(x) = x + 2

def f(x):
    y = x + 2
    return y

def f2(x):
    return x + 2


print(f(1))
print(f2(1))
y = f(1)
print(z)


'''



'''
lst1 = [2, 3, 4]
lst2 = [3, 3, 3, 3, 3, 3, 3]

prt_element(lst1)
prt_element(lst2)
'''



'''
M = [[0, 0, 1], [1, 2, 2], [2, 0, 3], [3, 2, 4]]


row     col     val
0       0       1
1       2       2
2       0       3
3       2       4
'''
'''
row = [0, 1, 2, 3]
col = [0, 2, 0, 2]
val = [1, 2, 3, 4]

M = [[0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

M[1][2]
'''
'''
name = ['철수', '영희', '영수']
age = [1, 2, 3]
place = ['aaa', 'bbb', 'ccc']

for n, a, p in zip(name, age, place):
    print('이름=', n, '나이=', a, '거주지=', p)
'''

'''
for iterator in sequence:
    do
'''
'''
for i in range(from이상, to미만, stepsize):
    do
'''

'''
- string
        + + : 두 스트링을 붙이기 (concatenate)
        + * : 반복하기
            - >>> "abc" * 3
                'abcabcabc'
        + length
            - len()
        + 위치 / 번째
            - index
                == 번째를 나타내는 숫자
                !!! 0부터 시작
            - "abcdef"[0] == "a"
        + indexing
            - index를 인풋으로 주고 index 번째의 문자를 꺼내오는 행위
            - "abcdef"[0] == "a"
        + slicing
            - index 범위 : [from 이상: to 미만]
            - s = 'abcdef'
                >>> s[0:2+1]
                'abc'
        + index 가져오기

            - 문자를 인풋으로 주고, 그 문자의 index를 가져오는 함수
            - index("내가 원하는 문자")
                >>> s.index("c")
                2
'''
'''

lst = ["a", "b", "c", "d"]

for e in lst:
    if e == "c":
        break
    print(e)
'''
'''
a
b
....
d



s = "abcd"



for idx in range(0, len(lst), 1):
    print(lst[idx])

print('-' * 10)

for idx in range(0, 3 + 1):
    print(lst[idx])

print('-' * 10)

for idx in [0, 1, 2, 3]:
    print(lst[idx])

print('-' * 10)
print("a")
print("b")
print("c")
print("d")
'''

'''
n = 1 + 2 + 3 + .... + 10 == 55

# n = 1 + 2 + 3+ 4  +% .....



i = 0
while i < 10:
    print(i)
    i = i + 1

'''

'''
x = 123413241324636

if x % 2 == 0:
    if x % 3 == 0:
        print("6의 배수이다")
'''
