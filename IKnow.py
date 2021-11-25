class IKnow:
    def __init__(self):
        pass
    def takeTurn(self, sInput):
        return "I know you are a " + sInput + " but what am I?"
    
if __name__ == '__main__':
    oGame = IKnow()

    while True:
        sInput = input("> ")
        sReturn = oGame.takeTurn(sInput)
        print(sReturn)
