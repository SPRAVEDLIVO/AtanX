import commands, hashlib
cmd = commands.Command()
@cmd.event(command="hash")
def hs(args):
    assert args != None
    assert len(args) >= 2
    hashtype = args[0]
    strtohash = " ".join(args[1:])
    # Procedural generated code goes here. See others/procedural_hashes.py
    if hashtype == 'sha3_512': return hashlib.new("sha3_512", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'sha3_384': return hashlib.new("sha3_384", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'md5': return hashlib.new("md5", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'mdc2': return hashlib.new("mdc2", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'blake2s': return hashlib.new("blake2s", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'sha256': return hashlib.new("sha256", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'md4': return hashlib.new("md4", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'md5-sha1': return hashlib.new("md5-sha1", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'blake2b512': return hashlib.new("blake2b512", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'ripemd160': return hashlib.new("ripemd160", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'shake_256': return hashlib.new("shake_256", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'sha384': return hashlib.new("sha384", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'sha1': return hashlib.new("sha1", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'sha224': return hashlib.new("sha224", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'blake2b': return hashlib.new("blake2b", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'whirlpool': return hashlib.new("whirlpool", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'sha3_256': return hashlib.new("sha3_256", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'sha512': return hashlib.new("sha512", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'sha3_224': return hashlib.new("sha3_224", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'shake_128': return hashlib.new("shake_128", strtohash.encode("utf-8")).hexdigest()
    elif hashtype == 'blake2s256': return hashlib.new("blake2s256", strtohash.encode("utf-8")).hexdigest()
    #EO procedural generated code.