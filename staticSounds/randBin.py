import numpy as n, music as m, os
from scipy.io import wavfile as w
H = m.utils.H
V = m.utils.V
# 1) propose random settings, write them to file
# 2) read file to synth with settings

def mkBin(fl=[200], fr=[240], a=[.8], aa=.8, t=10, fname='binaural', sr=44100, forms=['sine']):
    ts = 60*t
    if len(a) != len(fl):
        a = a*len(fl)
    sl = n.zeros(ts*sr)
    sr_ = n.zeros(ts*sr)
    for f, a_, form in zip(fl, a, forms):
        if form in ('sine', 0):
            s = n.linspace(0, ts*f*2*n.pi, ts*sr, endpoint=False)
            sl += n.sin(s) * a_
        elif form in ('saw', 1):
            sl += a_ * (n.linspace(0, ts*f*2, ts*sr)%2 * 2 - 1)
    for f, a_, form in zip(fr, a, forms):
        if form in ('sine', 0):
            s = n.linspace(0, ts*f*2*n.pi, ts*sr, endpoint=False)
            sr_ += n.sin(s) * a_
        elif form in ('saw', 1):
            sr_ = a_ * (n.linspace(0, ts*f*2, ts*sr)%2 * 2 - 1)

    sl_ = aa * 2 * ( (sl - sl.min()) / (sl.max() - sl.min()) -0.5 )
    sr_ = aa * 2 * ( (sr_ - sr_.min()) / (sr_.max() - sr_.min()) -0.5 )

    w.write(fname + '.wav', sr, V(sl_, sr_).T)
    os.system('sox ' + fname + '.wav ' + fname + '.flac')
    os.system('rm ' + fname + '.wav')

    w.write(fname + '_.wav', sr, (sl_+sr_)*.5)
    os.system('sox ' + fname + '_.wav ' + fname + '_.flac')
    os.system('rm ' + fname + '_.wav')
def randSet(mins=1, maxs=8, minf=20, maxf=800, mina=.02, maxa=1, minb=0.1, maxb=80):
    nsounds = n.random.randint(mins,maxs+1)
    fs = n.random.uniform(minf, maxf, nsounds)
    as_ = n.random.uniform(mina, maxa, nsounds)
    forms = n.random.randint(0,2,nsounds) # 0 is sine, 1 is saw
    fbeat = n.random.uniform(minb, maxb)
    fl = []
    fr = []
    i = 0
    for f in fs:
        if i%2 == 0:
            fl.append(f)
            fr.append(f+fbeat)
        else:
            fl.append(f+fbeat)
            fr.append(f)
        i += 1
    fname = ('s'+'%.2f_'*len(fs)+'__%.2f-'+'%.2f'*nsounds) % (*list(fs), fbeat, *list(as_))
    mkBin(
        fl,
        fr,
        as_,
        fname=fname,
        forms=forms
    )
    print(
        '\nfl,         ', fl,
        '\nfr,         ', fr,
        '\nas_,        ', as_,
        '\nfname=fname,', fname,
        '\nforms=forms ', forms
    )
    print(fname, 'written')



