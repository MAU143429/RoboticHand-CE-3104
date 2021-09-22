from Software.Lexical_Analysis.Tokenize import *
from Software.Semantic.BooleanValue import *
import pprint

from Software.Semantic.Generate_Error import Generate_Error


class SymbolsTable:
    def __init__(self):
        self.table = {}
        self.mainCounter = 0
        self.exist = False

    def Clean(self):
        self.table = {}
        self.mainCounter = 0

    def insertToken(self, key, name):
        key = str(key)
        if key == "ID":
            exist = False
            for var in self.table:
                if var == name:
                    exist = True
                    break
            if not exist:
                self.table[name] = {
                    "type": None,
                    "value": None,
                    "scope": None,
                }
                print("Soy: " + str(name))

        elif key == "MAIN":
            self.mainCounter += 1
            self.table[name] = {
                "cantidad": self.mainCounter,
                "Scope": "Main block",
            }
        else:
            pass

    def insertValue(self, value, name, line):
        exist = False
        for var in self.table:
            if var == name:
                if self.table[name]["value"] == None:
                    pass
                else:
                    exist = True
                    return True

        if not exist:
            t_value = value
            if isinstance(value,int):
                self.table[name]["value"] = t_value
                self.table[name]["type"] = int
            elif isinstance(validate_real_bool(value),bool):
                self.table[name]["value"] = validate_bool(t_value)
                self.table[name]["type"] = bool
            else:
                for var in self.table:
                    # let sum = 49;
                    # let sum = var1;
                    if var == str(value):
                        new_value = self.table[var]["value"]
                        self.table[name]["value"] = new_value
                        if isinstance(new_value, int):
                            self.table[name]["type"] = int
                        elif isinstance(validate_real_bool(new_value), bool):
                            self.table[name]["type"] = bool
                            t_value = new_value

                if t_value == value:
                    errorHandler = Generate_Error(5, line)
                    errorHandler.Execute()
        return False

    def printTable(self):
        pprint.pprint(self.table)
