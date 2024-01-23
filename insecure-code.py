import hashlib

sha = hashlib.sha1()
sha.update(b'trololo')
print(sha.hexdigest())

sha = hashlib.sha1()
sha.update(b'tutatyadssada')
print(sha.hexdigest())

sha = hashlib.sha1()
sha.update(b'tutatyadssada')
print(sha.hexdigest())
