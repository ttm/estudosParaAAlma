import numpy as n
from scipy.io import wavfile as w
import music as m
H = m.utils.H
V = m.utils.V

def mkBin(fl=[200], fr=[240], a=[.8], aa=.8, t=10, fname='binaural', sr=44100):
    ts = 60*t
    if len(a) != len(fl):
        a = a*len(fl)
    sl = n.zeros(ts*sr)
    for f, a_ in zip(fl, a):
        s = n.linspace(0, ts*f*2*n.pi, ts*sr, endpoint=False)
        sl += n.sin(s) * a_
    sr_ = n.zeros(ts*sr)
    for f, a_ in zip(fr, a):
        s = n.linspace(0, ts*f*2*n.pi, ts*sr, endpoint=False)
        sr_ += n.sin(s) * a_

    sl_ = aa * 2 * ( (sl - sl.min()) / (sl.max() - sl.min()) -0.5 )
    sr_ = aa * 2 * ( (sr_ - sr_.min()) / (sr_.max() - sr_.min()) -0.5 )

    w.write(fname + '.wav', sr, V(sl_, sr_).T)
    w.write(fname + '_.wav', sr, (sl_+sr_)*.5)

mkBin(
    [100, 240, 400, 840, 1200],
    [140, 200, 440, 800, 1240],
    [1, .8, .6, .4, .2],
    fname='bin6',
    sr=192000
)
