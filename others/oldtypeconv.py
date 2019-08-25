import configparser
cfg = configparser.ConfigParser()
cfg.read_string("""
[ascii2text]
category = converters
description = Convert any string of ascii numbers to text
usage = &ascii2text <text>
""")
d = {}
for sec in cfg.sections():
    for opt in cfg.options(sec):
        if sec not in d.keys():
            d.update({sec:[opt]})
        else:
            d[sec].append(opt)
print(d)