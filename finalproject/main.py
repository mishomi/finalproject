import random

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
    return ""
def checkifnew(letters):
    a = input()
    if a == '':
        print("you should give us a non-empty letter")
        return checkifnew(letters)
    if len(a)>1:
        print("you should just input one letter")
        return checkifnew(letters)

    if a in letters:
        print(f"you have already tried letter {a}, try again")
        return checkifnew(letters)
    else:
        letters.append(a)
        return letters

def hangman():
    lives = 6
    random_word = ''
    with open('words.txt', 'r') as text:
        words = text.readlines()
        random_word = random.choice(words).strip()
    random_decoded = ''
    for i in random_word:
        random_decoded += '_'
    letters = []
    while lives > 0:
        print(drawState(6-lives))
        print(random_decoded)
        if random_word == random_decoded:
            print('congratulations, you won, do you want to try again? Y/N')
            a = input().lower()
            if a == 'y':
                return hangman()
            else:
                return
        print(f"you have {lives} lives, guess the letter")
        letters = checkifnew(letters)
        letter = letters[-1]
        found = False
        for i in range(len(random_word)):
            if random_word[i] == letter:
                random_decoded = random_decoded[:i] + letter + random_decoded[i+1:]
                found = True
        if not found:
            lives -= 1
    print('you lose, do you want to try again? Y/N')
    a = input().lower()
    if a == 'y':
        return hangman()
    else:
        return

hangman()