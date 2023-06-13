from src.models import retranscript, export
from src.views import view

models = ["tiny.en", "base.en", "small.en", "medium.en", "tiny", "base", "small", "medium", "large"]

class Controller():
    def __init__(self):
        self.view = view.View()
        self.view.set_controller(self)
        self.view.main_menu()

    def retranscript(self, path_audio = "", CHOICE_M = models[5]):
        if path_audio != "":
            self.view.loading()
            self.retranscript = retranscript.Retranscript(path_audio, CHOICE_M)
            self.view.stop_loading()
            self.result = self.retranscript.get_result()
            self.view.result(self.result)
        
        else:
            self.view.error("No audio file selected")

    def loading_return(self):
        self.retranscript = None
        self.view.stop_loading()
        self.view.main_menu()

    def result_return(self):
        self.retranscript = None
        self.view.main_menu()

    def save_result(self):
        filepath = self.view.save_file()
        if filepath != "":
            self.export = export.Export(filepath, self.result)
            self.view.saved()
        
        else:
            self.view.error("No file selected")

    def run(self):
        self.view.run()
