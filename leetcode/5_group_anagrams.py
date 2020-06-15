strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["hos","boo","nay","deb","wow","bop","bob","brr","hey","rye","eve","elf","pup","bum","iva","lyx","yap","ugh","hem","rod","aha","nam","gap","yea","doc","pen","job","dis","max","oho","jed","lye","ram","pup","qua","ugh","mir","nap","deb","hog","let","gym","bye","lon","aft","eel","sol","jab"]
# strs = ['']
a = {}
for s in strs:
    sa = ''.join(sorted(s))
    if sa in a:
        a[sa].append(s)
    else:
        a[sa] = [s]
return [a[s] for s in a]

# n = len(strs)
# res = []
# i = 0
# while i < n:
#     a = strs[i]
#     if strs[i] != '-':
#         res.append([a])
#     else:
#         i += 1
#         continue
#     for j in range(i + 1, n):
#         if strs[i] != '-' and set(strs[i]) == set(strs[j]):
#             res[-1].append(strs[j])
#             strs[j] = '-'
#     i += 1
# return res

a = [["hos"],["boo","bob"],["nay"],["deb","deb"],["wow"],["bop"],["brr"],["hey"],["rye"],["eve"],["elf"],["pup","pup"],["bum"],["iva"],["lyx"],["yap"],["ugh","ugh"],["hem"],["rod"],["aha"],["nam"],["gap"],["yea"],["doc"],["pen"],["job"],["dis"],["max"],["oho"],["jed"],["lye"],["ram"],["qua"],["mir"],["nap"],["hog"],["let"],["gym"],["bye"],["lon"],["aft"],["eel"],["sol"],["jab"]]
b = [["sol"],["wow"],["gap"],["hem"],["yap"],["bum"],["ugh","ugh"],["aha"],["jab"],["eve"],["bop"],["lyx"],["jed"],["iva"],["rod"],["boo"],["brr"],["hog"],["nay"],["mir"],["deb","deb"],["aft"],["dis"],["yea"],["hos"],["rye"],["hey"],["doc"],["bob"],["eel"],["pen"],["job"],["max"],["oho"],["lye"],["ram"],["nap"],["elf"],["qua"],["pup","pup"],["let"],["gym"],["nam"],["bye"],["lon"]]
print([x for x in b if x not in resa])