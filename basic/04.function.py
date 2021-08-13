age = "18"
print(age)
print(type(age))
n_age = int(age)
print(n_age)
print(type(n_age))

#define function
def say_hello():
    print("hello")
    print("bye")

say_hello()

#arguments
def say_hello(who):
    print("hello", who)

say_hello("Nicolas")

def plus(a, b):
    print(a + b)

def minus(a, b=0):
    print(a - b)

plus(2, 5)
minus(2, 1)