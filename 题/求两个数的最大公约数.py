# 两个正整数a和b（a>b），它们的最大公约数等于a除以b的余数c和b之间的最大公约数。
# 辗转相除法
# 思路：
# 1.将两整数求余 a%b = x
#
# 2.如果x = 0;则b为最大公约数
#
# 3.如果x != 0,则 a = b；b = x；继续从1开始执行
#
# 4.也就是说该循环的是否继续的判断条件就是x是否为0
def fun1(a,b):
    x = a % b
    while (x != 0):
        a = b
        b = x
        x = a % b
    return b
def fun(a,b):
    a = max(a,b)
    b = min(a,b)
    if a%b == 0:
        return b
    for i in range(b//2,1,-1):
        if b % i == 0 and a % i == 0:
            return i
# print(fun(20,8))

# 更相减损法
# 思路：
# 1.如果a>b ，a = a - b;
#
# 2.如果b>a ，b = b - a;
#
# 3.假如a = b ，则 a或b  是最大公约数
#
# 4.如果a != b,则继续继续相减，直至a = b
def fun2(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b

#辗转相除法
def get_max_commen_divisor2(a,b):
    x = a%b
    while (x != 0):
        a = b
        b = x
        x = a % b
    return b
print(get_max_commen_divisor2(10,20))


# 枚举法
# 思路：
# 1.选出a，b中最小的一个数字放到min中
#
# 2.分别用a，b对i求余数，即看是否能被整除
#
# 3.直到a，b同时都能被i整除
#
# 4.如不能整除，i加一 继续开始执行，直到i等于min
def fun3(a,b):
    if a < b:
        min = a
    else:
        min = b
    i = 1
    while i < min:
        if a % i == 0:
            if b % i == 0:
                x = i
        i += 1
    return x