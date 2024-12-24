import math
def removeComments(filepath):

    f1=open(filepath,"r")
    content=f1.read()
    totalchar=len(content)
    writeflag=1
    newcontent=""
    i=0
    
    while(i<totalchar):
        if(content[i:i+2]=="/*"):
            writeflag=0
            i+=2
        elif(content[i:i+2]=="*/"):
            writeflag=1
            i+=2
        elif(writeflag):
            newcontent+=content[i]
            i+=1
        else:
            i+=1

    f1.close()
    print(newcontent)
    f2=open(filepath,"w")
    f2.write(newcontent) 
    f2.close()
    print("Done")



while True:
    filepath=input("Please enter file path: ")
    removeComments(filepath)
    ask=input("Wanna continue?(y/n): ")
    if(ask not in ["y","Y"]):
        break

