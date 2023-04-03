# Exercise 1 - communication
from pepper_seminar.speech_synthesis import TextToSpeech

class Exercise1:

    def __init__(self, intro) -> None:
        self.intro = intro

    def exercise1(self,intro):
        text_to_speech = TextToSpeech()
        text_stop = "Pauziramo vježbu onda"
        text_continue = "Nastavljamo vježbu onda"
        
    
