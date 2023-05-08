# Exercise 1 - communication
from speech_recognition import SpeechToText
from speech_synthesis import TextToSpeech
import time
import random

class Exercise1:

    # def __init__(self, intro1) -> None:
    #     self.intro = intro1

    def exercise1(self,intro1):
        text_stop = "Pauziramo vježbu onda"
        text_continue = "Nastavljamo vježbu onda"

        # TODO
        #making list of phrases for commenting exercise
        #executing exercise in loop of 10 
        #correcting PEPPER's behaviour regarding the answer (YES/NO)

        phrases = [ "Je li vam izvođenje vježbe prebrzo?", "Boli li Vas prilikom izvođenja?", "Hoćete li da ponovimo vježbu?",]
        counting = ["jedan", "dva", "tri", "četiri", "pet", "šest", "sedam", "osam", "devet", "deset"]
        comments = ["Ajmooo, radite rukama kao da pokušavate ugrabiti sto eura", "Samo nastavite tako!", "Ajmo Đurđa, mrdaj te rukice"]
        ends = ["Uh, baš sam se umorio. Ali došli smo do kraja ponavljanja! Bravo ekipa! Idemo na sljedeću vježbu.", "Završili smo s ovom vježbom. Slobodno uzmite kratki predah. Nemamo vremena za puš-pauzu, ali dok ja brbljam o sljedećoj vježbi popijte malo vode.", "Svaka čast društvo, uspješno smo završili ponavljanje. Malo odmorite pa krećemo sa sljedećom vježbom." ]

        #intro
        text_to_speech_intro = TextToSpeech(intro1).synthesize_speech()
        speech_to_text = SpeechToText()

        for i in counting:
            
            text_to_speech = TextToSpeech(i).synthesize_speech()
            time.sleep(3)

            if i == "tri":
                TextToSpeech(random.choice(comments)).synthesize_speech()

            elif i == "šest":

                TextToSpeech(random.choice(phrases)).synthesize_speech()
                stt = speech_to_text.recognize_from_microphone()
                print(stt)
                if stt == "Da.":
                    TextToSpeech(text_stop).synthesize_speech()
                    #ends exercise or change the speed of executing
                    time.sleep(5)
                elif stt == "Ne.":
                    TextToSpeech(text_continue).synthesize_speech()
                    continue

            elif i == "osam":
                TextToSpeech(random.choice(phrases)).synthesize_speech()
                stt = speech_to_text.recognize_from_microphone()
                if stt == "Da.":
                    TextToSpeech(text_stop).synthesize_speech()
                    #ends exercise or change the speed of executing
                    time.sleep(5)    
                elif stt == "Ne.": 
                    TextToSpeech(text_continue).synthesize_speech()
                    continue
        
        #end of exercise
        TextToSpeech(random.choice(ends)).synthesize_speech()


#introduction to pacient
TextToSpeech("Dobar dan, moje ime je Pepper. Ja sam humanoidni robot čija je zadaća danas demonstrirati vam rehabilitacijske vježbe ramena. Ja se pomalo bojim bolnica i doktora, ali danas sam došao samo zbog vas kako bih vam pomogao u vašem oporavku. Naš današnji zadatak je prodrmati malo ta ramena i vidjeti kako vaša rehabilitacija napreduje. Pored sebe imate papir s glasovnim porukama koje meni olakšavaju evaluaciju vašeg izvođenja. Prilikom vježbi postavljat ću vam pitanja na koje ćete vi odgovarati prema uputama. Molio bih vas da koristite fraze koje su navedene jer nažalost nisam još toliko pametan da bih mogao prepoznati druge odgovore. Ajmo se sada bacit' na posao!").synthesize_speech()

#first exercise
exercise1 = Exercise1()                
exercise1.exercise1("Ova vježba se sastoji od odvajanja ruku od tijela i spajanja istih iznad glave. Ponovit ćemo ju deset puta nakon čega slijedi kratki predah.")

print("uspjelo")

    

    

        
    
