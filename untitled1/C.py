import calc

num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))

print("{0} + {1} = {2} 입니다".format(num1, num2, calc.sum(num1, num2)))
print("{0} - {1} = {2} 입니다".format(num1, num2, calc.sub(num1, num2)))
print("{0} * {1} = {2} 입니다".format(num1, num2, calc.mul(num1, num2)))
print("{0} / {1} = {2:5.3f} 입니다".format(num1, num2, calc.div(num1, num2)))

