def checking(guess):
    print("is your number", guess,"?", end=" ")
    a = input().lower()
    return a

def binary_search(list):
    lowerL = 0
    upperL = len(list) - 1
    
    while lowerL <= upperL:
        half = int((lowerL + upperL) / 2)
        guess = list[half]
        
        if (round_result := checking(guess)) == 'correct':
            print("YAY!")
            break
        if round_result == 'lower':
            upperL = half - 1
        else:
            lowerL = half + 1
    else:
        print('you lying.... ')

numeros = [k for k in range(0,10001)]

print("Choose a number between 0 and 10000. and i'll guess it in less than 15 tries!")
print("Respond with 'lower', 'higher' or 'correct'")
input("\tpress enter to continue")
binary_search(numeros)