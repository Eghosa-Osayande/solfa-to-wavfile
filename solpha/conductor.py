from .part import Part

class Cfg():
    '''
    Cfg contains the settings read from the
    solfa score
    '''
    def __init__(self,TITLE, TONIC, TONIC_PITCH, BPM, PARTS, TIME_SIGNATURE, SCORE):
        self.TITLE=TITLE
        self.TONIC=TONIC
        self.TONIC_PITCH=TONIC_PITCH
        self.BPM=BPM
        self.PARTS=PARTS
        self.TIME_SIGNATURE= TIME_SIGNATURE
        self.SCORE=SCORE
        
class Conductor():
    '''
    The conductor is responsible for parsing 
    the contents of the solfa score and retrieving 
    important settings for the song.
    This class also serves as the cordinator for the different parts
    '''
    letters='C Cs D Ds E F Fs G Gs A As B'.lower().replace(' ',',').split(',')
    _scale= None
    _raw_score=None
    
    def __init__(self, data):
        self.config=self.process_data(data)
        self.key= self.config.TONIC.lower()
        self.pitch= self.config.TONIC_PITCH
        self.bpm= self.config.BPM
        self.song_title = self.config.TITLE
        parts= self.config.PARTS
        self.parts=[]
       
        for part in parts:
            self.parts.append(Part(
                name=part['name'],
                id= part['id'],
                volume=part['volume'],
                instrument=part['instrument'],
                config=self.config,
            ))
    
    @property    
    def scale(self,*a):
        '''
        returns dict containing the solfa notes and their corresponding letters
        '''
        if self._scale:
            return self._scale
        ref= self.letters.index(self.key)
        new_scale=t=self.letters[ref:]+self.letters[:ref]
        scale ={
            'd':new_scale[0], 'de':new_scale[1],
            'r':new_scale[2], 're':new_scale[3], 
            'm':new_scale[4], 'f':new_scale[5], 
            'fe':new_scale[6], 's':new_scale[7], 
            'se':new_scale[8], 'l':new_scale[9], 
            'le':new_scale[10], 't':new_scale[11],
            'ta':new_scale[10], 'soh':new_scale[6], 
            'ma':new_scale[3], 'ra':new_scale[1],
            '-':'-', 'x':'x' 
        }
        self._scale=scale
        return scale
    
    def process_data(self,data):
        '''
        parses the solfa score and returns the Cfg class containing the required settings
        '''
        exec(data, globals())
        c=Cfg(TITLE, TONIC, TONIC_PITCH, BPM, PARTS, TIME_SIGNATURE, SCORE)
        return c
    
    def get_solfa(self):
        '''
        returns list of lists containing notes for respective parts
        '''
        return [p.get_solfa() for p in self.parts]
    
    @property
    def raw_score(self,*a):
        '''
        returns score as a list containing each line
        '''
        if self._raw_score:
            return self._raw_score
        score=self.config.SCORE
        self._raw_score=score.splitlines()
        return self._raw_score 
    
    def get_music_code(self):
        '''
        step 1 
        Conductor asks,       
        'Parts check for errors
        if any raise error
        else set your sheet'
        #TODO
        '''
        results=[]
        for part in self.parts:
            results.append(part.set_sheet(self.raw_score))
        if False in results:
            print('syntax error')
            
        '''
        Step 2
        Conductor says,
        Parts read your sheet
        tell me each note and its duration
        '''
        instructions=[]
        for part in self.parts:
            part.read_sheet(self.key,self.pitch,self.bpm,self.scale)
        
        
        
            
