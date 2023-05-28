import hashlib

def first(secret):
    i = 1
    while True:
        code = hashlib.md5((secret + str(i)).encode('utf-8')).hexdigest()
        #print(code)
        if code.startswith('000000'):
            return i
        i+= 1


print(first('bgvyzdsv'))
