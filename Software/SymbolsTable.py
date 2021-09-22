from Software.Lexical_Analysis.Tokenize import *
from Software.Semantic.BooleanValue import validate_bool
import pprint


class SymbolsTable:
    def __init__(self):
        self.table = {}
        self.mainCounter = 0

    def Clean(self):
        self.table = {}
        self.mainCounter = 0

    def insertToken(self, key, name):
        key = str(key)
        if key == "ID":
            self.table[name] = {
                "type": None,
                "value": None,
                "scope": None,
            }

        elif key == "MAIN":
            self.mainCounter += 1
            self.table[name] = {
                "cantidad": self.mainCounter,
                "Scope": "Main block",
            }
        else:
            pass

    def insertValue(self, value, name):
        exist = False
        print("SOY EL VALUE ----> "+ str(value))
        for var in self.table:
            if var == name:
                if self.table[name]["value"] == None:
                    pass
                else:
                    exist = True

        if not exist:
            t_value = value
            for var in self.table:
                if var == str(value):
                    new_value = self.table[var]["value"]
                    t_value = new_value

            if validate_bool(t_value):
                self.table[name]["value"] = validate_bool(t_value)
                self.table[name]["type"] = bool
            else:
                self.table[name]["value"] = t_value
                self.table[name]["type"] = int






    def printTable(self):
        pprint.pprint(self.table)




# mySymbolsTable = SymbolsTable()
# mySymbolsTable.insertToken("var1")
# mySymbolsTable.insertToken("var2")
# mySymbolsTable.insertToken("var3")
# mySymbolsTable.insertToken("var4")
# mySymbolsTable.insertToken("main")
# mySymbolsTable.insertToken("main")
# print(mySymbolsTable.table)
