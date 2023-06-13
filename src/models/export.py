class Export():
    def __init__(self, path, data):
        self.path = path
        self.data = data
        self.export()

    def export(self):
        with open(self.path, "w") as file:
            file.write(self.data)