import whisper

class Retranscript():
    def __init__(self, path_audio, CHOICE_M):
        self.CHOICE_M = CHOICE_M

        self.model = whisper.load_model(CHOICE_M)

        self.path_audio = path_audio

        self.pad_or_trim()
        self.log_mel_spectrogram()
        self.retranscript()

    def pad_or_trim(self):
        # load audio and pad/trim it to fit 30 seconds
        self.audio = whisper.load_audio(self.path_audio)
        self.audio = whisper.pad_or_trim(self.audio)

    def log_mel_spectrogram(self):
        # make log-Mel spectrogram and move to the same device as the model
        self.mel = whisper.log_mel_spectrogram(self.audio).to(self.model.device)

    def detect_language(self):
        # detect the spoken language
        _, probs = self.model.detect_language(self.mel)
        return max(probs, key=probs.get)

    def retranscript(self):
        # decode the audio
        options = whisper.DecodingOptions()
        self.result = whisper.decode(self.model, self.mel, options)

    def get_result(self):
        return self.result.text