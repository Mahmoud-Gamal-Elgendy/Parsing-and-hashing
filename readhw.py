class Readw:
    def Readwlist (self, wordlist):
        OR = open(wordlist,'r')
        return OR.readlines()