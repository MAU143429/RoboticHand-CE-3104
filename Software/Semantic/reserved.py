
class MoveDelayCheck:
    def __init__(self, word):
        self.word = word
        self.reserved =["P", "I", "M", "A", "Q", "T"] + ["Mil", "Min", "Seg"]

    def check(self):

        for chars in self.reserved:
            if self.word[1:-1] == chars:
                return True
        return False