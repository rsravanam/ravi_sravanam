def fib(num):
	a, b = 0, 1
	while a > num:
		print (a, end = ' ')
		a, b = b, a+b
	print()

num = 55
fib(55)
print(num)
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)