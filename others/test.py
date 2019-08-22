import hashlib
def hs(args):
    assert args != None
    assert len(args) >= 2
    hashtype = args[0]
    strtohash = " ".join(args[1:])
    # Procedural generated code goes here. See others/procedural_hashes.py
    if hashtype == 'sha256': sub = hashlib.new("sha256"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'sha3_256': sub = hashlib.new("sha3_256"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'sha3_384': sub = hashlib.new("sha3_384"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'md5': sub = hashlib.new("md5"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'ripemd160': sub = hashlib.new("ripemd160"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'blake2b512': sub = hashlib.new("blake2b512"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'sha224': sub = hashlib.new("sha224"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'mdc2': sub = hashlib.new("mdc2"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'blake2s256': sub = hashlib.new("blake2s256"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'blake2s': sub = hashlib.new("blake2s"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'sha3_512': sub = hashlib.new("sha3_512"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'sha3_224': sub = hashlib.new("sha3_224"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'sha1': sub = hashlib.new("sha1"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'sha512': sub = hashlib.new("sha512"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'blake2b': sub = hashlib.new("blake2b"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'whirlpool': sub = hashlib.new("whirlpool"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'md5-sha1': sub = hashlib.new("md5-sha1"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'shake_128': sub = hashlib.new("shake_128"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'sha384': sub = hashlib.new("sha384"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'shake_256': sub = hashlib.new("shake_256"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    elif hashtype == 'md4': sub = hashlib.new("md4"); sub.update(strtohash.encode("utf-8")); return sub.hexdigest()
    #EO procedural generated code.
print(hs(["md5", "kolbasa"]))