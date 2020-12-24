'''
script to convert tonic solfa to .wav file
''' 

import pygame as pg
from time import sleep
from solpha.conductor import Conductor
from solpha.producer import Producer

filename='nostalgia.py'
fd=open(filename,'r')
cont=fd.read()
fd.close()
Chijoke =c= Conductor(cont) 
Chijoke.get_music_code()
print(c.get_solfa())
music = Producer.produce(Chijoke.parts) 

M=pg.mixer
C=M.Channel
S=M.Sound

M.init(frequency=music.frame_rate, size=-16, channels= 1,buffer= 2048)
pg.init()

j=S(music.raw_data).play(loops=10)
music.export('nostalgia.wav',format='wav')

while True:
    pass
  