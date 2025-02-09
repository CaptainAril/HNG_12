val = '371'

int(val)  # 153

length = len(val)

final = sum([int(i) ** length for i in val])

print(final)

print(final == int(val))

