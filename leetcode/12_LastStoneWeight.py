stones = [4,3,4,3,2]

if len(stones) == 2:
    print('else', max(stones) - min(stones))

if len(stones) == 1:
    print(stones[0])

while len(stones) >= 1:
    if len(stones) > 2:
        max1 = max(stones)
        new_stones = [i for i in stones ]
        new_stones.remove(max1)
        max2 = max(new_stones)
        print(max1, max2, new_stones)
        
        if max1 == max2:
            stones.remove(max1)
            stones.remove(max1)
        else:
            max1 = stones.index(max1)
            max2 = stones.index(max2)
            stones[max1] = stones[max1] - stones[max2]
            stones.remove(stones[max2])
    else:
        if len(stones) == 2:
            ans = max(stones) - min(stones)
            stones = [ans]
        else:
            ans = stones[0]
        break

    print(max1, max2, stones)

print(ans)
