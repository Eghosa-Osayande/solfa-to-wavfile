import numpy as np
import sys 
sys.path.append('../')
from pydub import AudioSegment as Seg
import pygame as pg
from time import sleep
import sound_plot as sp

con=np.concatenate
M=pg.mixer
C=M.Channel
S=M.Sound





snd=Seg.from_wav(sp.f3)
snd2=Seg.from_wav('violin/e1.wav')
arr=snd.sndarray
print(snd.duration_seconds,arr.shape,)

b=snd2.append(snd2, crossfade=2000).append(snd2, crossfade=2000).append(snd2, crossfade=2000).append(snd2, crossfade=2000).append(snd2, crossfade=2000)

#exit()
M.init(frequency=b.frame_rate, size=-16, channels= 1,buffer= 2048)
pg.init()
j=S(b.raw_data).play(loops=1)
b.export('trr.wav',format='wav')

while True:
    pass 
    