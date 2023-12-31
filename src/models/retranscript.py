import whisper
from threading import Thread

class Retranscript():
    def __init__(self, path_audio, CHOICE_M):
        self.success = False
        self.result = None
        self.thread = None
        self.CHOICE_M = CHOICE_M
        self.path_audio = path_audio

        try:
            # self.thread = Thread(target=self.transcribe)

            self.thread = Thread(target=self.retranscript)
        
        except Exception as e:
            self.result = str(e)

    def pad_or_trim(self):
        # load audio and pad/trim it to fit 30 seconds
        self.audio = whisper.load_audio(self.path_audio)
        self.audio = whisper.pad_or_trim(self.audio)

    def log_mel_spectrogram(self):
        # make log-Mel spectrogram and move to the same device as the model
        self.mel = whisper.log_mel_spectrogram(self.audio).to(self.model_detect.device)

    def detect_language(self):
        # detect the spoken language
        _, probs = self.model_detect.detect_language(self.mel)
        self.language = max(probs, key=probs.get)

    #def decode(self):
        # decode the audio
    #    options = whisper.DecodingOptions(fp16=True)
    #    self.result = whisper.decode(self.model, self.mel, options)

    def retranscript(self):
        try:
            self.model_detect = whisper.load_model(name="base")

            self.pad_or_trim()
            self.log_mel_spectrogram()
            self.detect_language()

            model = whisper.load_model(name=self.CHOICE_M)
            options = whisper.DecodingOptions(fp16=True, language=self.language)

            self.result = model.transcribe(self.path_audio)
            self.result = self.result["text"]

            self.success = True
        
        except Exception as e:
            self.result = str(e)

    def transcribe(self):
        try:
            model = whisper.load_model(name=self.CHOICE_M)

            self.result = model.transcribe(self.path_audio, fp16=False)
            self.result = self.result["text"]

            self.success = True
        
        except Exception as e:
            self.result = str(e)

    def get_result(self):
        return self.result
    
    def get_thread(self):
        return self.thread

    def set_controller(self, controller):
        self.controller = controller