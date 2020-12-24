

class Note():
    '''
    class representing a sound to be made 
    by a part
    '''
    def __init__(self, start, end, solfa, pitch,bpm,scale,config):
        self.config=config
        self.start=start
        self.end=end
        self.solfa=solfa
        self.pitch=pitch
        self.bpm=bpm
        self.duration=self.get_duration(start,end)
        self.note= self.get_letter(solfa,scale)
        self.extensions=[] 
        self.prev=None
        self.next=None
        self.type= self.get_type(solfa)
        self.sound=None

    def __str__(self):
        return self.note
    
    def make_sound(self,instrument):
        '''
        sets the sound made by the note
        '''
        self.sound=instrument.play(self,self.config)    
            
    @property
    def length(self,*a):
        return self.duration *1000
    
    def do_extension(self,child):
        '''
        extends the note longer than a second
        '''
        self.duration+=child.duration
        self.extensions.append(child)
    
    def is_silent(self):
        return True if self.type == 'silence' else False
        
    def get_type(self,solfa):
           if solfa == 'x':
               return 'silence'
           elif solfa == '-':
               return 'extension'
           else:
               return 'normal'
           
    def get_letter(self,solfa,scale):
        ##TODO
        #Edit Later
        try:
            return scale[solfa]
        except:
            print(f'error')
      
    def get_duration(self,start,end):
        '''
        get duration of note based on the mode the tonic solfa was written, either dynamic or static
        Currently I have implementes the feature to switch from dynamic to static,
        Currently set to dynamic
        '''
        dur=end
        #dur=start+end
        if dur in (':'):#('::', ':|', '|:', ':|', '||'):
            return 60/self.bpm
        
        if dur in ('.'):#(':.', '.|', '|.', '.:'):
            return (60/self.bpm)* .5
        
        if dur in (','):#(':,', ',:', ',|', '|,', '.,', ',.'):
            return (60/self.bpm)* .25

