from src.models import retranscript, export
from src.views import view
from src.controllers.thread_monitor import Monitor

models = ["tiny.en", "base.en", "small.en", "medium.en", "tiny", "base", "small", "medium", "large", "large-v1", "large-v2"]

class Controller():
    def __init__(self):
        self.view = view.View()
        self.view.set_controller(self)
        self.view.main_menu()

    def retranscript_load(self, path_audio, CHOICE_M):
        if path_audio != "" and CHOICE_M in models:
            try:
                self.view.loading()
                
                self.retranscript = retranscript.Retranscript(path_audio, CHOICE_M)
                self.retranscript.set_controller(self)

                self.monitor = Monitor(self.retranscript.get_thread(), self.retranscript_finish)
                self.monitor_thread = self.monitor.get_thread()
                self.monitor_thread.start()
            
            except Exception as e:
                self.view.error(e)
        
        else:
            self.view.error("No audio file selected or no model selected")

    def retranscript_finish(self):
        self.view.stop_loading()

        if self.retranscript.success:
            self.result = self.retranscript.get_result()
            self.view.result(self.result)
        
        else:
            self.view.error(self.retranscript.get_result())

    def loading_return(self):
        self.monitor_thread = None
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