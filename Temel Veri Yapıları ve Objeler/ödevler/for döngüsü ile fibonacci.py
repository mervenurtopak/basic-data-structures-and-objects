print("""
****************
FİBONACCİ DİZİSİ
****************
""")
x=1
y=1
fibonacci= [x,y]
for i in range (10):
    x, y = y, x+y
    print("x:", x, "y:", y)

    fibonacci.append (y)

print(fibonacci)