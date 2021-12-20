f1=open("a.txt","r")
f2=open("b.txt","w")
for i in f1:
    f2.write(i)
f1.close()
f2.close()