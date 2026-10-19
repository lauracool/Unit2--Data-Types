 #def spaces(N,Y,T):
     #count = 0
    #for i in range(N):
        #if Y[i] == "C" and T[i] == "C":
            #count+=1
    #return count 
# print(spaces(6, "CC..CC", ".CC..C"))


t = 0 
s= 0 

for i in range(3):
    text = input()

    for letter in text:
        if letter == "t" or letter == "T":
            t+=1
        if letter == "s" or letter == "S":
            s+=1

    if t > s:
        print("English")
    elif s > t:
        print("French")
    elif t == s:
        print("French")
    else:
        print("None")













