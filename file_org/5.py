f1=open("a.txt","r")
f2=open("b.txt","r")
i=0
for j in f1:
    i+=1
    for k in f2:
        if j==k:
            print("same")
            break
        else:
            print("not same")
    break
f1.close()
f2.close()