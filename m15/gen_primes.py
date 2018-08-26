
def is_prime(n):
    i = 2
    while (i**2 <= n):
        if n%i == 0:
            return False
        i += 1
    return True
    

def gen_primes():
    p = 2
    yield p
    while True:
        p += 1
        if is_prime(p):
            yield p
        
        
    
    
p = gen_primes()

for i in range(0,5):
    print(p.__next__())
    
    