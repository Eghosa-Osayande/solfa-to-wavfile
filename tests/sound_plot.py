import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import sys 
sys.path.append('../')
from  pydub import AudioSegment as Seg

con=np.concatenate

style.use('dark_background')
f1='violin/c2.wav'
f2='violin/c3.wav'
f3='violin/c4.wav'
f4='violin/c5.wav'
f5='violin/c6.wav'


snd1=Seg.from_wav(f1).sndarray
snd2=Seg.from_wav(f2).sndarray
snd3=Seg.from_wav(f3).sndarray
snd4=Seg.from_wav(f4).sndarray
snd5=Seg.from_wav(f5).sndarray

fig,ax=plt.subplots(figsize=(10,5))
ax.axis('equal')
ax.grid(True)
ax.set_ylim([np.min(snd1),np.max(snd1)])
ax.xaxis.set_ticks(np.arange(0,snd1.shape[0],snd1.shape[0]/24))
ax.tick_params(
    axis="x", #labelsize=18,
    labelrotation=-90,
    labelcolor="turquoise")

ax.plot(snd1[:,0]+200000)
ax.plot(snd2[:,0]+100000)
ax.plot(snd3[:,0])
ax.plot(snd4[:,0]-100000)
ax.plot(snd5[:,0]-200000)
plt.show()
#plt.savefig('violin_notes_plot.png')