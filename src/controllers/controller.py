from src.models import retranscript, export
from src.views import view
from threading import Thread

models = ["tiny.en", "base.en", "small.en", "medium.en", "tiny", "base", "small", "medium", "large", "large-v1", "large-v2"]

class Controller():
    def __init__(self):
        self.view = view.View()
        self.view.set_controller(self)
        self.view.main_menu()

    def retranscript_load(self, path_audio, CHOICE_M):
        if path_audio != "" and CHOICE_M in models:
            self.retranscript = retranscript.Retranscript(path_audio, CHOICE_M)
            self.retranscript.set_controller(self)

            self.thread = Thread(target=self.retranscript.start)
            self.thread.start()
            self.view.loading()
        
        else:
            self.view.error("No audio file selected or no model selected")

    def retranscript_finish(self):
        self.thread.join()
        self.view.stop_loading()

        if self.retranscript.success:
            self.result = self.retranscript.get_result()
            self.view.result(self.result)
        
        else:
            self.view.error(self.retranscript.get_result())

    def loading_return(self):
        self.thread._stop()
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