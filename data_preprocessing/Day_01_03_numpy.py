import numpy as np
import random
a = np.arange(0, 5, 1)
print(a)
print(type(a))

a1 = np.arange(12)                                  # 12행짜리
a2 = np.arange(12, dtype=np.float32).reshape(3, 4)  # 3행 4열로 만든다
a3 = np.arange(12).reshape(2, 2, 3)                 # 2행 3열짜리 2개
print(a1)
print(a2)
print(a3)

print(a1.shape, a1.dtype, a1.size)
print(a2.shape, a2.dtype, a2.size)
print(a3.shape, a3.dtype, a3.size)
print("="*80)
# 0~5 사이의 정수를 갖는 2행 3열 배열을 만드세요

a1 = np.arange(6).reshape(2, 3)
print(a1)

b = np.array([0, 1, 2, 3, 4, 5]).reshape(2, 3)
print(b)

b = np.array([[0, 1, 2], [3, 4, 5]])
print(b)

print("="*80)
a1 = np.zeros(12, dtype=np.float32).reshape(3, 4)
print(a1.ndim, a1.shape, a1.size, a1.dtype, a1.itemsize, a1.data)
print(a1)
a1 = np.ones(12, dtype=np.float32).reshape(3, 4)
print(a1.ndim, a1.shape, a1.size, a1.dtype, a1.itemsize, a1.data)
print(a1)
a1 = np.empty(12, dtype=np.float32).reshape(3, 4)
print(a1.ndim, a1.shape, a1.size, a1.dtype, a1.itemsize, a1.data)
print(a1)
a1 = np.full((3, 4), 0.5)
print(a1.ndim, a1.shape, a1.size, a1.dtype, a1.itemsize, a1.data)
print(a1)

print(np.arange(0, 2, 0.25))             # 0~2까지 0.25씩 증가
print(np.linspace(0, 2, 10))             # 0~2까지 10등분한다
print("="*80)
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
print(a+b)
print(a**2)
print(a > 1)
print(np.sin(a))
print(a > b)
print("="*80)

c = np.arange(6).reshape((3, 2))
print(c)
print(c+1)
print(c**2)
print(np.logical_and(c > 0, c < 3))
print(np.logical_or(c > 0, c < 3))

d = np.arange(6, 12).reshape(3, 2)
print(c)
print(d)

print(c+d)

# 리스트로 배열을 만들면 계산이 불가능하다
e = [[0, 1, 2], [3, 4, 5]]
f = [[6, 7, 8], [9, 10, 11]]

print(e+f)

# 만들어진 리스트를 다시 np를 이용해 계산가능하게 할 수 있다.
print("="*80)
e = np.array(e)
f = np.array(f)
result = e + f
print(result)
print(type(e), type(f), type(result))

e = e.tolist()
f = f.tolist()
result = result.tolist()
print(type(e), type(f), type(result))

# 리스트를 받아서 연산을 하고 다시 리스트로 보내는 함수


def list_oper(list_1, list_2, oper):
    list_1_np = np.array(list_1)
    list_2_np = np.array(list_2)
    if oper == "+":
        result = list_1_np + list_2_np
    elif oper == "*":
        result = list_1_np * list_2_np
    elif oper == "-":
        result = list_1_np - list_2_np
    elif oper == "/":
        result = list_1_np / list_2_np
    list_1 = list_1_np.tolist()
    list_2 = list_2_np.tolist()
    result = result.tolist()
    return result

def list_make(row, col):
    result_list = []
    for i in range(0, row):
        col_list = []
        for j in range(0, col):
            cnt = random.randrange(1, 99)
            col_list.append(cnt)
        result_list.append(col_list)
    print(result_list)
    return result_list

list_1 = [[1,2,3], [4,5,6]]
list_2 = [[4,5,6], [7,8,9]]
list_a = list_make(4, 5)
list_b = list_make(4, 5)

result_list = list_oper(list_a, list_b, "+")
print("+결과", result_list)
result_list = list_oper(list_a, list_b, "*")
print("*결과", result_list)
result_list = list_oper(list_a, list_b, "-")
print("-결과", result_list)
result_list = list_oper(list_a, list_b, "/")
print("/결과", result_list)


# result_list = list_oper(list_1, list_2, "+")
# print("+결과", result_list)
# result_list = list_oper(list_1, list_2, "*")
# print("*결과", result_list)
# result_list = list_oper(list_1, list_2, "-")
# print("-결과", result_list)
# result_list = list_oper(list_1, list_2, "/")
# print("/결과", result_list)

print("="*80)
a = np.arange(3)                        # [0, 1, 2]
b = np.arange(6)                        # [0, 1, 2, 3, 4, 5]
c = np.arange(3).reshape(-1, 3)         # [[0, 1, 2]]
d = np.arange(6).reshape(-1, 3)         # [[0, 1, 2], [3, 4, 5]]
e = np.arange(3).reshape(3, -1)         # [[0], [1], [2]]

print(a+d)
print(a+c)
print(c+d)
print("=====")
print(a+e)
print(b+e)
print(c+e)
print(d+e)
