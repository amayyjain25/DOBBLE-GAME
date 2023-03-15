# ALPHABETS AS COMMON
# DEFINATE NO. OF SYMBOLE
# ONLY 1 COMMON ALPHABET
import random
import string

symbol = []
symbol = list(string.ascii_letters)
card1 = [0] * 5
card2 = [0] * 5
pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)
pont = 0

# pos1 and pos2 are same position in card 1 and card 2 respectively
samesymbol = random.choice(symbol)
symbol.remove(samesymbol)
if (pos1 == pos2):
    card2[pos1] = samesymbol
    card1[pos2] = samesymbol
else:
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol
    card1[pos2] = random.choice(symbol)
    symbol.remove(card1[pos2])
    card2[pos1] = random.choice(symbol)
    symbol.remove(card2[pos1])
i = 0
while (i < 5):
    if (i != pos1 and i != pos2):
        alphabet1 = random.choice(symbol)
        symbol.remove(alphabet1)
        alphabet2 = random.choice(symbol)
        symbol.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i += 1
print(card1)
print(card2)
ch = input("Spot the similar symbol")
if ch == samesymbol:
    print("you are correct")
else:
    print("sorry, you are wrong", samesymbol)


