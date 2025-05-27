marks=[58, 89.25, 15, 80, 65]
# print(marks)
# print(marks[2])
# for i in marks:
#     print(i)

for i in range(0,5):
    print(marks[i], end=" ")
print("")
m=[[1,2,3],[4,5,6],[7,8,9]]
# print(m)
for i in range(0,3):
    for j in range(0,3):
        print(m[i][j], end=" ")
    print("")

print(marks[1:])
print(marks[1:4])
print(marks[:4])