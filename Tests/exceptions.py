#a.
class NotABinaryStringException(Exception):
    def __init__(self,msg):
        self.msg = msg
num = input("Enter a Binary String")
def gen_dec(num):
    val = 0
    for n in num:
        if n == '0':
            val = val * 2
        elif n == '1':
            val = val * 2 + 1
        else:
            raise NotABinaryStringException("This is not Binary !")
    yield val

try:
    x = gen_dec(num)
    print(x.__next__())
except NotABinaryStringException as n:
    print(n.msg)
else:
    print("Binary")


#b.
class ResultNotAnIntegerException(Exception):
    def __init__(self,message):
        self.message = message
num1 = int(input("Enter Number 1 : "))
num2 = int(input("Enter Number 2 : "))
try:
    ans = num1/num2
    if (ans != int(ans)):
        raise ResultNotAnIntegerException("Answer is not integer")
except ResultNotAnIntegerException as r:
    print(r.message)
else:
    print("Result is an integer")



