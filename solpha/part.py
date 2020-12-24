
from .note import Note
from .instrument import Instrument

time_markers={ ':': 1, '.': 0.5, ',': 0.25, '|': 1}

class Part():
    '''
    Class representing a part in the music 
    '''
    def __init__(self,**kwargs):
        self.name= kwargs.get('name')
        self.id= kwargs.get('id')
        self.volume= kwargs.get('volume')
        self.instrument= kwargs.get('instrument')
        self.config= kwargs.get('config')
        _raw_score= None
        self.notes = None 
    
    def get_solfa(self):
        '''
        returns list containing tuples of solfa, duration and relative pitch
        '''
        return [(n.solfa,n.duration,n.pitch) for n in self.notes]
    
    def make_music(self):
        '''
       converts list of notes to AudioSegment class containing the data of sound to make
        '''
        music=None
        for note in self.notes:
            note.make_sound(Instrument(self.instrument))
            if music == None:
                music= note.sound
            else:
                music+=note.sound
        return music            
    
    def read_sheet(self, key, pitch, bpm, scale):
        
        '''
        this function reads the solfa notation and returns list of notes
        
        '''
        
        notes=[]
        start=''
        _pitch=''
        pitch=0
        solfa=''
        end=''

        for char in self.sheet:
            if char in time_markers.keys():
                if start != '' :
                    end=char
                    if solfa != '':
                        n=Note(start,end,solfa,pitch,bpm,scale,self.config)                    
                        if solfa=='-':
                            notes[-1].do_extension(n)
                        else:
                            if len(notes)>0:
                                prev=notes[-1]
                                n.prev=prev
                                prev.next=n 
                            notes.append(n)
                            
                        start=''
                        _pitch=''
                        pitch=0
                        solfa=''
                        end=''
                        
                start=char
                continue
            if char.isalpha() or char=='-' or char =='x':
                solfa+=char
                
            if char =="'":
              _pitch+=char
              pitch= len(_pitch)*-1 if solfa == '' else len(_pitch)*1
              
        self.notes= notes      
    
    def set_sheet(self, raw_score):
        '''
        sets the sheet for the part
        and chexks if there is any error
        '''
        self._raw_score=r=raw_score
        raw_sheet=r= self._get_raw_sheet()
        sheet= self.check_syntax(raw_sheet)
        self.sheet=sheet     
        return sheet if sheet else False
        
    def check_syntax(self,score):
        #TODO
        #False means error
        return score #False
    
    def _get_raw_sheet(self):
        
        raw_sheet=''
        for line in self._raw_score:
            line=line.replace('\t','').replace(' ','').replace('\n','')
            if line.startswith(self.id):
                line=line.replace(self.id,'')
                raw_sheet+=line
        
        return raw_sheet