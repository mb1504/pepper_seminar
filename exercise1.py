# Exercise 1 - communication
from speech_recognition import SpeechToText
from speech_synthesis import TextToSpeech

class Exercise1:

    def __init__(self, intro1) -> None:
        self.intro = intro1

    def exercise1(self,intro1):
        text_to_speech = TextToSpeech()
        text_stop = "Pauziramo vježbu onda"
        text_continue = "Nastavljamo vježbu onda"

    text_to_speech = TextToSpeech()
    speech_to_text = SpeechToText()

    # TODO
    #making list of phrases for commenting exercise
    #executing exercise in loop of 10 
    #correcting PEPPER's behaviour regarding the answer (YES/NO)

    phrases = ["Je li vam brzina izvođenja odgovarajuća?", "Boli li Vas prilikom izvođenja?","Možete li nastaviti?"]
    counting = ["jedan", "dva", "tri", "četiri", "pet", "šest", "sedam", "osam", "devet", "deset"]
   
    #intro
    text_to_speech.speechSynthesis(intro1)

    

        
    
