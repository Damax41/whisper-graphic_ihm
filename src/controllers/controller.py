from src.models import retranscript, export
from src.views import view
from threading import Thread

models = ["tiny.en", "base.en", "small.en", "medium.en", "tiny", "base", "small", "medium", "large"]

class Controller():
    def __init__(self):
        self.view = view.View()
        self.view.set_controller(self)
        self.view.main_menu()

    def retranscript(self, path_audio, CHOICE_M):
        if path_audio != "" and CHOICE_M in models:
            self.retranscript = Thread(target=retranscript.Retranscript, args=(path_audio, CHOICE_M))
            self.retranscript.start()
            self.view.loading()
            self.retranscript.join()
            self.view.stop_loading()

            if self.retranscript.exitcode == 0:
                self.result = self.retranscript.result()
                self.view.result(self.result)
            
            else:
                self.view.error("An error occured during the retranscription")
        
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
