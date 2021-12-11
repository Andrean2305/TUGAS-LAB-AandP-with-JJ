import random
a,b = 2,3
while a != b :
    print("Try again bro\nMaybe choose different difficulties?")
    x = input("Choose the difficulties :PUSI(TYPE A) // PRO(TYPE B) // MACHOMAN(TYPE C) !!! please type with uppercase :)\n")
    print(f"So you choose {x}")
    if x == "A" :
     a = random.randint(1,5)    #a = angka acak yang dipilih dalam perjudian ini
    elif x == "B" :
     a = random.randint(1,20) 
    elif x == "C" :
     a = random.randint(1,100)
    input("______________________________________________")
    input("■■■■■■■■■■■□□□  NOWLOADING")
    input("Oke already loaded, just click enter")
    if x == "A" :
        b = int(input("Choose a number between 1-5\n"))
    elif x == "B" :
        b = int(input("Choose a number between 1-20\n")) 
    elif x == "c" :
        b = int(input("Choose a number between 1-100\n"))
    print(f"Oke you're guessing {b} right? Now lets see are you goint to win")
    input("Click enter again")
    if b == a :
        print("WOW LUCKIEST PERSON, CONGRATS\n♬°⋆⋆°♬ (○^ω^ )_旦~~♪🎓🎓♬°⋆⋆°♬")
    else :
        print("You are wrong\n︵‿︵(´ ͡༎ຶ ͜ʖ ͡༎ຶ `)︵‿︵")
        print("The number is ",a)