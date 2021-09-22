class MoveDelayCheck:
    def __init__(self, word):
        self.word = word
        self.fingers = ["P", "I", "M", "A", "Q", "T"]
        self.units = ["Mil", "Min", "Seg"]

    def check_fingers(self):
        if isinstance(self.word,list):
            cont = 0
            found = False
            while(cont < len(self.word)):

                for chars in self.fingers:
                    print(self.word)
                    if self.word[cont][1:-1] == chars:
                        found = True
                        break

                if found == False:
                    return False
                else:
                    found = False
                    cont += 1

            return True
        else:
            for chars in self.fingers:
                if self.word[1:-1] == chars:
                    return True
            return False

    def check_units(self):
        for chars in self.units:
            if self.word[1:-1] == chars:
                return True
        return False