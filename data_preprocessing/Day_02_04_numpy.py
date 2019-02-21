import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)

b = np.arange(12).reshape(-1, 4)
print(b)

print("="*100)
list_1 =["딸기", "사과", "배", "포도", "복숭아"]
a = np.random.choice(list_1, 5, replace=False)          # replace=Flase를 하면 중복제거를 해줌
print(a)

a = np.random.choice(range(100), 12, replace=False)
a = np.reshape(a, [3,4])
print(a)

b = np.arange(12).reshape(-1, 4)
print(b)

print(np.sum(b))                    # 요소 전체의 합
print(np.sum(b, axis=0))            # 열끼리 합한다 (수직)
print(np.sum(b, axis=1))            # 행끼리 합한다 (수평)

print(a)
print(a.max())
print(a.max(axis=0))                # 열중에 가장 큰 값
print(a.max(axis=1))                # 행중에 가장 큰 값

print(a)
print(a.min())
print(a.min(axis=0))                # 열중에 가장 작은 값
print(a.min(axis=1))                # 행중에 가장 작은 값

print(b)
print(b.std(), b.var(), b.mean())   # mean 은 평균
print("="*100)

print(b)
b[0] = -1
print(b)

b[1:3] = 99
print(b)
print("===")

print(b[::2])
print(b[0:3:2])         # 0행과 2행만 출력됨 0~3-1행까지 2행
print("="*100)

a = np.random.choice(range(100), 12, replace=False)
a = np.reshape(a, [3,4])
b = np.arange(12).reshape(-1, 4)
print(a)
print(b)
print(a+b)
print(list(a) + list(b))
print(np.array(list(a) + list(b)))                  # nump array 합치기

print(np.vstack([a,b]))                             # 수직합치기
print(np.hstack([a,b]))                             # 수평합치기
print("="*100)

a = np.arange(12).reshape(-1,4)
print(a[-1][-1], a[0][0])
print("="*100)
# 2차원 배열을 거꾸로 출력해주세요:
print(a[::-1])
print("="*100)

print(a[0, 0], a[-1, -1])
print(a[:2, :2])
print(a[::-1, ::-1])

print("="*100)
print(a)
print(a[1:3, 1:3])

print("="*100)
print(a)
print(a[0:3, 2:4])


print(a[3::-1])

# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 1 1 1 1

a = np.ones([4, 5], dtype=np.int32)
print(a)
a[1:3, 1:4] = 0                         # 1행1열 부터 3행 4열까지 0으로
print(a)
print("="*100)

# 1 1 1 1 0
# 1 1 1 0 1
# 1 1 0 1 1
# 1 0 1 1 1
# 0 1 1 1 1
# 1행 5열
# 2행 4열
# 3행 3열
# 4행 2열
# 5행 1열
a = np.ones([7, 7], dtype=np.int32)
print(a)
row, col = a.shape                  # shape 함수는 행 열의 값을 리턴한다
print("row = " , len(a))
print("col = " , len(a[0]))
for i in range(row):
        a[i, (col-1)-i] = 0
        a[i, i] = 0

print(a)
