sample = [1, 2, 3, 4, 5, 6]

squares = []
for x in sample:
    squares.append(x**2)
squares

print(squares)

print([x**2 for x in sample if x % 2 == 0])
print([x**2 if x % 2 == 0 else -x for x in sample])

print({x: x**2 if x % 2 == 0 else -x for x in sample})

print({x for x in [1, 2, 1, 2, 3, 2, 1]})

print(tuple(x**2 if x % 2 == 0 else -x for x in sample))
