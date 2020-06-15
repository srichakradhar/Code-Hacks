a = 0
b = 8
c = 11
count_dict = {'a': a, 'b': b, 'c': c}
happy_string = ''
counts = [a, b, c]
while sum(counts) > 0:
    ranks = sorted([(a, i) for (i, a) in count_dict.items()], key=lambda x: -x[0])
    counts = []
    symbols = []
    for count, symbol in ranks:
        counts.append(count)
        symbols.append(symbol)
    counts = [i for i in counts if i != 0]
    # print(counts, happy_string)
    if len(counts) == 1 and happy_string[-2:] == symbols[0] * 2:
        break
    i = 0
    for j in range(len(counts)):
        if happy_string[-2:] == symbols[i] * 2:
            i = 1
        if counts[i] >= 2:
            happy_string += symbols[i] * 2
            counts[i] -= 2
        elif counts[i] == 1:
            happy_string += symbols[i]
            counts[i] -= 1
        count_dict[symbols[i]] = counts[i]
        if i == 1:
            break
    
print(happy_string)