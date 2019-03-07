import numpy as n
from scipy.io import wavfile as w
import music as m
H = m.utils.H
V = m.utils.V


f1 = 178
f1 = 38
f1 = 100
f2 = 182
f2 = 42
f2 = 140

t = 10  # min
ts = t*60
a = .2

s = n.linspace(0, ts*f1*2*n.pi, ts*44100)
ss = n.sin(s)*a
s = n.linspace(0, ts*f2*2*n.pi, ts*44100)
ss2 = n.sin(s)*a
w.write('s40.wav', 44100, V(ss, ss2).T)
w.write('s40_.wav', 44100, (ss+ss2)*.5)




