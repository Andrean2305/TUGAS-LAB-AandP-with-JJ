def diamond(a): 
    width = (a+1)/2
    for i in range (a) : 
        
        if i >= width :
            b = " " * (i+1)
            c = "o" * ((2*a)-1-(i*2))
        else:
            b = " " * (a-i)
            c = "o" * (i*2+1)

        print(f"{b}{c}") 

zeee = eval(input("State the height of the diamond(Input odd number for better result): "))
a = diamond(zeee)
