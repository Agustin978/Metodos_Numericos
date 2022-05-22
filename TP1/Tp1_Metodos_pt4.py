from math import e
func = 0
x = 0
for n in range(1,21):
    x = 10**(-n)
    func = (e**x - e**(-x))/(2*x)
    print(func)