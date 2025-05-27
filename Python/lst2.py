m=[56,99.99, 80, 87.25, 60]
print(len(m))
print(min(m))
print(max(m))
print(sum(m))
m.append(92)
print(m)
m.pop()
print(m)
m.remove(80)
print(m)
m.sort()
print(m)

m.sort(reverse=True) # DESC to ASC
print(m)