import os
from .pydub_custom import AudioSegment 

def list_instruments():
    '''
    returns list of current instruments 
    so far, I only added violin, but I dont plan on adding any other soon
    '''
    instru_names= os.listdir(os.path.join('instruments'))
    return instru_names

def set_sound_duration(sound, length):
    unit= int(len(sound))
    if length < unit:
        sound = sound[:length]
    elif length == unit:
        sound = sound
    elif length > unit:        
        crossfade_value=int(unit/2)
        diff= length - unit
        freq= int((diff/2)+1) if unit % 2 else int(diff/2)
        for i in range(freq):
            sound=sound.append(sound,crossfade=crossfade_value)
        sound=sound[:length]
    return sound        
    

class Instrument():
    letters='C Cs D Ds E F Fs G Gs A As B'.lower().replace(' ',',').split(',')
    
    def __init__(self,path):
        self.directory=os.path.join('solpha','instruments',path)
        notes= os.listdir(self.directory)
        self.octaves= [x.replace('.wav','') for x in notes ]
        self._frame_rate= None
        
    def play(self,note,config):
        offset=0
        tonic=config.TONIC.lower()
        if tonic != 'c':
            special_keys=self.letters[:self.letters.index(tonic)]
            if note.note in special_keys:
                offset=1
            
        key='{}{}.wav'.format(note.note, note.pitch + config.TONIC_PITCH+ offset)
        
        if note.is_silent():
            sound=AudioSegment.silent(duration=note.length, frame_rate= self.frame_rate)         
        
        else:
            sound= AudioSegment.from_file(os.path.join(self.directory,key))
            sound=set_sound_duration(sound, note.length)

        return sound
    
    @property
    def frame_rate(self,*a):
        if self._frame_rate == None:
            self._frame_rate= AudioSegment.from_file(os.path.join(self.directory,self.octaves[0]+'.wav')).frame_rate
        return self._frame_rate
            
    
    
            