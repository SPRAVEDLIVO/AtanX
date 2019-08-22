import hashlib
n = ""
for alg in hashlib.algorithms_available:
    n+= "if hashtype == \'{0}\': return hashlib.new(\"{0}\", strtohash.encode(\"utf-8\")).hexdigest()\n".format(alg)
print(n)