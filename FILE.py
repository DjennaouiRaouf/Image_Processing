class FILE:

    def __init__(self):
        self.file=list()

    def ENFILER(self, item):
        self.file.append(item)

    def DEFILER(self):
        if len(self.file)<1:
            return None
        return self.file.pop(0)

    def FILE_VIDE(self):
        return len(self.file)==0