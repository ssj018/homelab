counts = {}
try:
    while True:
        id, key, value = input().split()
        value = int(value)
        try:
            tmp = counts[key]
        except KeyError:
            tmp = counts[key] = {}
        try:
            tmp[id] += value
        except KeyError:
            tmp[id] = value
except:
    pass


for k, v in counts.items():
    v = list(v.items())
    v.sort(key=lambda x:x[1], reverse=True)
    counts[k] = v

counts = list(counts.items())
counts.sort(key=lambda x:x[0])
for k, v in counts:
    max_value = v[0][1]
    for id, value in v:
        if value == max_value:
            print(id, k, value)