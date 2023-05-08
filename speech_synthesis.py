import os
import azure.cognitiveservices.speech as speechsdk

class TextToSpeech:
    def __init__(self, text):
        self.text = text
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        self.speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        # The language of the voice that speaks.
        self.speech_config.speech_synthesis_voice_name='hr-HR-SreckoNeural'
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=self.audio_config)

    def synthesize_speech(self):
        speech_synthesis_result = self.speech_synthesizer.speak_text_async(self.text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(self.text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")

# Example usage:
#tts = TextToSpeech("Hello, world!")
#tts.synthesize_speech()
