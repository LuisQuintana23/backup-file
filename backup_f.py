import os.path as osp
from datetime import date, datetime

class Backup():

    def __init__(self, path):
        self.path = path
        self.date = datetime.now().strftime("%Y_%m_%d_%H:%M")

    def backup(self):
        pass

    def create_folder(self, name):
        pass



if __name__ == "__main__":
    route = osp.abspath("./test.psd")
    print(route)
    back1 = Backup(route)