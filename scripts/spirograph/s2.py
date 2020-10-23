import numpy as n, pylab as p

t = n.linspace(0, 100, 10000)
x = n.sin(t * 15.1)
y = n.cos(t * 5)

p.plot(x, y)
p.show()
