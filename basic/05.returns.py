def p_plus(a, b):
    print(a + b)

def r_plus(a, b):
    return a + b

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)

def r_pluss(a, b):
    return a + b
    print("like this")

rr_result = r_pluss(2, 3)
print(rr_result) 
# one function can use one return
# if use return that function is exit

# can use keyworded argument
def r_plusss(a, b):
    return a - b
result = r_plusss(b=30, a=2)
print(result)
