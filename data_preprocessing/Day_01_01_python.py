print("test")
a=10
b=20
c= 30
print(a+b)
print(c//b)     # 몫 만 출력
print(c/b)
print("hello" + "python")
print("="*80)

age = 15
print(10 < age < 19)
print(10 > age)
print("="*80)
print(True and True)
print(True and False)
print(True or False)

print("="*80)
print(12, 3.14, "he", True)
print(type(12), type(3.14), type("he"), type(True))

print("="*80)
for i in range(1, 6):
    print("*"*i)

print("="*80)
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")


# teacher
s = ""
for i in range(1, 6):
    s += str(i) + " "
    print(s)

print("="*80)
a = [1, 3, 5]

print(a[0], a[-1], a[1], a[-2], a[len(a)-1])

b = "collection: list, tuple, dictionary"
print(len(b)/2)
print(b[0:(len(b)//2)], b[(len(b)//2)+1:])
print(b[::-1])


def f_1(a1, a2):
    return a1 + a2, a1 - a2

a, b = 3, 5
ret = f_1(a, b)
print(ret)
print(type(ret))
print("="*80)

tuple_ret = (1, 2, 3, 4, 5)
list_ret = list(tuple_ret)
print(tuple_ret)
list_ret[0] = 10
print(list_ret)
tuple_ret = tuple(list_ret)
print(tuple_ret)

print("="*80)


def StringToList(list_val):
    str_val = ""
    for i in list_val:
        str_val += i
    return str_val


str_a = "collection: list, tuple, dictionary"
list_a = list(str_a)
print(str_a)
print(list_a)
str_a = str(list_a)
print(str_a)
str_b = StringToList(list_a)
print(str_b)

print("="*80)
print(12, 34, 56)
print(12, 34, 56, sep="**")
print(12, 34, 56, end="==")
print("")
print(12, 34, 56, sep="**", end="==")
