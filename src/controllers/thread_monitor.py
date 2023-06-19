from threading import Thread

class Monitor():
    def __init__(self, thread, return_function):
        self.thread = thread
        self.return_function = return_function
        
        self.monitor()
    
    def monitor(self):
        self.monitor_thread = Thread(target=self.start)
    
    def start(self):
        self.thread.start()
        self.thread.join()
        self.return_function()

    def get_thread(self):
        return self.monitor_thread