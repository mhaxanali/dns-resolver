from datetime import datetime

class Log:

    def __init__(self, name):
        self.name = name

    def warning(self, text):
        print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | [WARNING] | {self.name} | {text}")

    def fatal(self, text):
        print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | [FATAL] | {self.name} | {text}")

    def info(self, text):
        print(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | [INFO] | {self.name} | {text}")