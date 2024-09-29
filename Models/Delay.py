
class Delay():

    def __init__(self):
        self.__delay = {}

    def setDelay(self, tempo):
        self.__delay["delay"] = tempo
    
    def getDelay(self):
        return self.__delay