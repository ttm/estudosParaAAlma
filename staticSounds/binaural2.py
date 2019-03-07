import numpy as n
from scipy.io import wavfile as w
import music as m
H = m.utils.H
V = m.utils.V


f1 = 100
f1_ = 240
f2 = 140
f2_ = 200

t = 10  # min
ts = t*60
a = .2

s = n.linspace(0, ts*f1*2*n.pi, ts*44100)
ss = n.sin(s)*a
s = n.linspace(0, ts*f1_*2*n.pi, ts*44100)
ss = n.sin(s)*a + ss

s = n.linspace(0, ts*f2*2*n.pi, ts*44100)
ss2 = n.sin(s)*a
s = n.linspace(0, ts*f2_*2*n.pi, ts*44100)
ss2 = n.sin(s)*a + ss2


w.write('s40_2.wav', 44100, V(ss, ss2).T)
w.write('s40_2_.wav', 44100, (ss+ss2)*.5)




