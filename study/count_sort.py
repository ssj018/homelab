
# c z 7
# b z 2
# c x 1
# a z 3
# a x 1
# b y 5
# a x 4
# a y 1
# b x 3
# c y 1
# b z 3
# b y 2
# c x 8
# c x 2
# b x 1
# c y 2
# a y 2
# a z 7
# a x 1
# b x 1
# c z 1
# ...

# c z 7
# b z 2
# a z 3
# b y 2
# c x 8
# c x 2
# b x 1
# c y 2
# a y 2
# a z 7
# ...

counts = {}
id_sum = {}

print('Please enter your input. use \'...\' to stop:')
while True:
    lines = input()
    if lines == '...':
        break
    
    id,tp,score = lines.split()
    score = int(score)
    
    if not counts.get(tp):
        counts[tp] = {}
    if not counts[tp].get(id):
        counts[tp][id] = 0
    
    counts[tp][id] += score
   
    print(counts)

counts = list(counts.items())
counts.sort(key=lambda x: x[0])

for k,v  in counts:
    max_key = max(v, key=v.get)
    print(max_key, k, v[max_key])
        