
class MoveDelayCheck:
    def __init__(self, word):
        self.word = word
        self.reserved =['P', 'I', 'M', 'A', 'Q', 'T'] + ['Mil', 'Min', 'Seg']

    def check(self):

        for chars in self.reserved:
            print(chars)
            print(self.word)
            if self.word == chars:
                return True
        return False