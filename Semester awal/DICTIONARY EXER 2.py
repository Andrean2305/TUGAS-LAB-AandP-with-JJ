a = eval(input("Enter the number of people(at least 5): "))
while a<5 :
    a = eval(input("Enter again your number too low: "))

za = []
zc = []
for i in range (1,a+1) :
    b = input(f"Enter the name({i}): ")
    za.append(b)

    zb = []
    favourite = eval(input("Enter numbers of his/her favourite cars: "))
    while favourite < 3:
        favourite = eval(input("Enter again our number too low: "))
    for i in range (1,favourite+1) :
        c = input("Enter her/his favourite cars: ")
        zb.append(c)
    zc.append(zb)

mydict = {} #buat jadi dict
for i in range (a) :
    mydict.update({za[i] : zc[i]})

#if you are too busy to input alot of things kindly use my handmade dict
#don't forget to # input code

#mydict = {
#    "jj" : ['Golf', 'Camry', 'LFA'] ,  
#    "Nickolas" : ['Gold', 'Camrt', 'LFS'] ,
#    "Andrean" : ['Golz', 'Camrr', 'LFD'] ,
#    "Hasan" : ['Golx', 'Cammm', 'LFF'] , 
#    "Permata" : ['Golzz', 'Camkk', 'LFZ'] ,
#}

for key in mydict.keys() :
    print(f"{key} like these cars:")
    for value in mydict[key] :
        print("-",value) #For output the key and value from the dictionary