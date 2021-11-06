data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

designations = []
codes = []
for i in data:
    if i[0] == '0':
        codes.append(i)
    else:
        designations.append(i)
operators = dict(zip(designations, codes))
[operators.pop(key) for key in ["Katel", "Fonex"]]

operators['O!'] = {"0500", "0700", "0708"}
operators['Megacom'] = {"0550", "0999", "0555"}
operators['Beeline'] = {"0770", "0222", "0777"}

for key, value in operators.items():
    print(f"{key}-{value}")
