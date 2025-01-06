n = 4
x = ""
def gen(i):
    global x
    for j in range(2):
        x = x + str(j)
        if i == n:
            print(x)
        else:
            gen(i+1)
        x = x[:-1]
gen(1)