from datetime import datetime

class Log:

    def __init__(self, name):
        self.name = name

    def warning(self, text):
        print(f"{datetime.now()} | [WARNING] | {self.name} | {text}\n")

    def fatal(self, text):
        print(f"{datetime.now()} | [FATAL] | {self.name} | {text}\n")

    def info(self, text):
        print(f"{datetime.now()} | [INFO] | {self.name} | {text}\n")