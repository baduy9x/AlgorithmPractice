class Solution(object):
    def fib(self, n):
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        first = 1
        second = 1
        count = 0
        while count <=n:
            result = first + second
            first = second
            second = result
            count += 1

if __name__ == __main__: