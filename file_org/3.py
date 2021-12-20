f1=open("a.txt","r")
count=dict()
for line in f1:
    words=line.split()
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
print(count)
f1.close()