st = {"A":"Alpha","B":"Beta","C":"Charlie","D":"Delta","E":"Echo","F":"Foxstrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu", "-":"Dash", " ":"(space)"}
s = {}
for k, v in st.items():
    s.update({v:k})
print(s)