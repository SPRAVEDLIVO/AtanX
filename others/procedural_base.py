st = ""
for i in ["16", "64", "85"]:
    st+="if mode == \'{0}\':\n\treturn base64.b{0}decode(sub.encode(\"utf-8\").decode(\"utf-8\"))\n".format(i)
print(st)