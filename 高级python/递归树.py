import time

#斐波那切数列
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)



start = time.time()

print(fib(40))
end = time.time()
dur = end-start
print(dur)

#青蛙跳台阶 一共有n个台阶 每种台阶有两种跳法 n-1 和 n-2
def tiao(n):
    if n <= 2:
        return n
    return tiao(n-1)+tiao(n-2)

print(tiao(8))