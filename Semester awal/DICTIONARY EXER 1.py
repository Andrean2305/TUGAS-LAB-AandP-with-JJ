#z = {
#    "Python": "An interpreted, object-oriented, high-level programming language with dynamic semantics." , 
#    "C#": "A general-purpose, modern and object-oriented programming language pronounced as “C sharp." ,
#    "C": "A general-purpose, procedural computer programming language supporting structured programming.",
#    "HTML": "The set of markup symbols or codes inserted into a file intended for display on the Internet.",
#    "CSS": "the language for describing the presentation of Web pages, including colors, layout, and fonts."
#    }

#if you dont want to input just use the dict ^^^^
#and don't forget to # the input code
print("We can only do 5 language with this pattern (-odd, +even, -odd, +even)")
za = []
zc = []
for i in range (1,6) :
    b = input(f"Enter the programming language({i}): ")
    za.append(b)
    c = input(f"What is {b}?\n") #when input the desc of the language please don't just input 1 letter ex : a 
    zc.append(c)

z = {} #buat jadi dict
for i in range (5) :
    z.update({za[i] : zc[i]})

print(" ")

a = list(z) #getting the key as a list
number = []
for i in range (1,6) :
    number.append(i)

baaaz = 2
for oddeven in number :
    if oddeven % 2 == 1 :
        ba = a[baaaz]
        baaaz = baaaz - oddeven
        print (ba)
        print (z[ba],"\n")
    else :
        ba = a[baaaz]
        baaaz = baaaz + oddeven
        print(ba)
        print(z[ba],"\n")

