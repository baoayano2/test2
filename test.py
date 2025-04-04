shoes = [int(i) for i in input().split()]
hide = []
for i in shoes:
    if (shoes.count(-i) == 0):
        hide.append(-i)

for i in hide:
    if (i > 0):
        print(f"Chiếc giày bên trái, kích cỡ {abs(i)}")
    else:
        print(f"Chiếc giày bên phải, kích cỡ {abs(i)}")
