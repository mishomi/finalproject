def drawState(state):
    if state == 0:
        print('   -----')
        print('   |   |')
        print('   |')
        print('   |')
        print('   |')
        print('   |')
    elif state == 1:
        print('   -----')
        print('   |   |')
        print('   |   O')
        print('   |')
        print('   |')
        print("   |")
    elif state == 2:
        print('   -----')
        print('   |   |')
        print('   |   O')
        print('   |   |')
        print('   |')
        print("   |")
    elif state == 3:
        print('   -----')
        print('   |   |')
        print('   |   O')
        print('   |  /| ')
        print('   |')
        print("   |")
    elif state == 4:
        print('   -----')
        print('   |   |')
        print('   |   O')
        print('   |  /|\ ')
        print('   |')
        print("   |")
    elif state == 5:
        print('   -----')
        print('   |   |')
        print('   |   O')
        print('   |  /|\ ')
        print('   |  /')
        print("   |")
    elif state == 6:
        print('   -----')
        print('   |   |')
        print('   |   O')
        print('   |  /|\ ')
        print('   |  / \ ')
        print("   |")
    return ''
def hangman():
    print(drawState(0))
    print(drawState(1))
    print(drawState(2))
    print(drawState(3))
    print(drawState(4))
    print(drawState(5))
    print(drawState(6))
hangman()