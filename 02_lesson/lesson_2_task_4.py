def fizz_buzz(n):
    for i in range(1, n+1):
        res = str(i)
        if i % 3 == 0:
            res = 'Fizz'
        if i % 5 == 0:
            if res == 'Fizz':
                res = 'FizzBuzz'
            else:
                res = 'Buzz'
    print(res)
