import os

inititive = {}

while True:
    text = input("Do something... :")
    if text == 'Q':
        quit()
    elif text != 'D':
        text = text.split()
        if float(text[1]) in inititive:
            text[1] = int(text[1]) + 0.1
            print(text[1])
        inititive[float(text[1])] = text[0]
    elif text == 'D':
        os.system('clear')
        for n in sorted(inititive, reverse=True):
            print(f"{inititive[n]} = {n}")
