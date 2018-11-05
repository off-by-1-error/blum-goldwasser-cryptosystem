from random import randint

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def decrypt(message, p, q, y):
    #rp = (p + 1 // 4)
    #rp = rp**(len(message))
    #rp = y**rp
    rp = pow(y, ((p+1)//4)**(len(message)), p)

    #print(rp)

    #rq = (q + 1 // 4)
    #rq = rq**(len(message))
    rq = pow(y, ((q+1)//4)**(len(message)), q)

    #print(rq)

    x0 = (q * modinv(q, p) * rp + p * modinv(p, q) * rq) % (p * q)


    print(x0)

    plaintext, y = encrypt(ciphertext, p*q)

    print(plaintext)
    

def encrypt(message, public_key):
    keystream = []
    x_vals = []
    ciphertext = ""

    x_vals.append(159201)

    r = randint(0, public_key)

    for i in range(0, len(message)):
        result = x_vals[i] ** 2
        result = result % public_key
        x_vals.append(result)

    print (x_vals)
#    print ("len of x_vals:", len(x_vals))
#    print ("len of n:", len(message))

    for i in range(0, len(x_vals)):
        keystream.append(x_vals[i] & 1)

    print (keystream)
    print ("len of keystream: ", len(keystream))

    for i in range(0, len(message)):
        ciphertext += str(keystream[i] ^ int(message[i]))
        
    print (ciphertext)
    return (ciphertext, x_vals[len(x_vals)-1])


n = 499 * 547

plaintext = "10011100000100001100"
print ("plaintext: ", plaintext)

ciphertext, y = encrypt("10011100000100001100", n)

decrypt(ciphertext, 499, 547, y)
