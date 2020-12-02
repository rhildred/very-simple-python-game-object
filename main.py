from IKnow import IKnow

oGame = IKnow()

while True:
    sInput = input("> ")
    sReturn = oGame.takeTurn(sInput)
    print(sReturn)
