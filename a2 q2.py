d = {}
 
for i in range(97, 97 + 26):
    d[chr(i)] = i
 
print(d)

# or


d = {chr(i):
    i for i in range(97, 97 + 26)}
print(d)