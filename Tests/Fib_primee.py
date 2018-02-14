def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
#f = fibonacci(5)g
for x in fibonacci(10):
    print(x)

print("-------------------------Prime Numbers-----------------------")
def prime_no(n1,n2):
    for i in range(n1,n2):
        if(i==1 or i==0):
            prime=False
        elif(i==2):
            yield 2
        else:
            prime = True
            j = 2
            while j < i and prime:
                #j=2
                if (i % j == 0):
                    prime = False
                j+=1
        if prime:
            yield i

for p in prime_no(1,20):
    print(p)

