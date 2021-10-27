def emirpcheck(a):
    b = str(a)
    c = list(b)
    c.reverse()
    aa = "".join(c)
    aaa = int(aa)

    for i in range(2,aaa):
        if aaa%i == 0 or aaa <=11:
            aaaa = 111111
            break
        else:
            aaaa = 9696
    if aaaa == 9696:
        print(a,aaa)
    else:
        print("False!")

    
a = emirpcheck(13)
b = emirpcheck(347)
c = emirpcheck(5)
d = emirpcheck(11)
e = (eval(input("input a prime number: ")))

for i in range(2,e):
        if e%i == 0 or e <=11:
            ee = 111111
            break
        else:
            ee = 9696
if ee == 9696 :
 e = emirpcheck(e)
else:
 print(f"{e} is not a prime number")