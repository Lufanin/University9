def all_variants(text):
    x = len(text)
    for i in range(1, x +1):
        for z in range(x - i + 1):
            yield text[z:z+i]


a = all_variants("abc")
for i in a:
    print(i)