s = "xqgwkiqpif"
shift = [[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]

right = 0
left = 0
for sh in shift:
    if sh[0] == 1:
        right += sh[1]
    else:
        left += sh[1]
n = len(s)
right = right % n
left = left % n
if right > left:
    shn = right - left
    ans = s[-shn:] + s[:-shn]
elif right < left:
    shn = left - right
    ans = s[shn:] + s[:shn]
else:
    ans = s

print(ans)