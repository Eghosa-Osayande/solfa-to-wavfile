

class Producer():
    
    @staticmethod
    def produce(parts):
        lead=None
        for part in parts:
            channel=part.make_music()
            if lead == None:
                lead= channel
            else:
                lead=lead.overlay(channel)

        return lead
            