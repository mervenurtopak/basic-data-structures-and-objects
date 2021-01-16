print("""
****************
FİBONACCİ DİZİSİ
****************
""")
x=1
y=1
fibonacci= [x,y]
for i in range (20):

    x, y = y, x+y
    fibonacci.append (y)

print(fibonacci)