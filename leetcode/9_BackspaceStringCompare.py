S = "ab#c"
T = "ad#c"
final_S = ""
final_T = ""
for i in S:
    if i == '#':
        final_S = final_S[:-1]
    else:
        final_S += i

for i in T:
    if i == '#':
        final_T = final_T[:-1]
    else:
        final_T += i
print(final_S == final_T)
