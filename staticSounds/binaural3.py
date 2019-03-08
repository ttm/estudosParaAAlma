import numpy as n, music as m, os
from scipy.io import wavfile as w
H = m.utils.H
V = m.utils.V

def mkBin(fl=[200], fr=[240], a=[.8], aa=.8, t=10, fname='binaural', sr=44100, form='sine'):
    ts = 60*t
    if len(a) != len(fl):
        a = a*len(fl)
    sl = n.zeros(ts*sr)
    sr_ = n.zeros(ts*sr)
    if form == 'sine':
        for f, a_ in zip(fl, a):
            s = n.linspace(0, ts*f*2*n.pi, ts*sr, endpoint=False)
            sl += n.sin(s) * a_
        for f, a_ in zip(fr, a):
            s = n.linspace(0, ts*f*2*n.pi, ts*sr, endpoint=False)
            sr_ += n.sin(s) * a_
    elif form == 'saw':
        for f, a_ in zip(fl, a):
            sl += a_ * (n.linspace(0, ts*f*2, ts*sr)%2 * 2 - 1)
        for f, a_ in zip(fr, a):
            sr_ = a_ * (n.linspace(0, ts*f*2, ts*sr)%2 * 2 - 1)

    sl_ = aa * 2 * ( (sl - sl.min()) / (sl.max() - sl.min()) -0.5 )
    sr_ = aa * 2 * ( (sr_ - sr_.min()) / (sr_.max() - sr_.min()) -0.5 )

    w.write(fname + '.wav', sr, V(sl_, sr_).T)
    os.system('sox ' + fname + '.wav ' + fname + '.flac')
    os.system('rm ' + fname + '.wav')

    w.write(fname + '_.wav', sr, (sl_+sr_)*.5)
    os.system('sox ' + fname + '_.wav ' + fname + '_.flac')
    os.system('rm ' + fname + '_.wav')

mkBin(
    [30],
    [30.2],
    [1, .8, .6, .4, .2],
    fname='saw0.2hz01',
    sr=192000,
    form='saw'
)
