########BINI#######BINI#######BINI########BINI###########BINI########BINI########
import sqlite3



con=sqlite3.connect("Dictionary.db")
c=con.cursor()

    

def find_qus(qus):#searching entry
    
    c.execute("SELECT definition FROM entries WHERE word  = '{}'".format(qus))
    
    ans=c.fetchone()
    if ans !=None:
        return ans
    else :
        return False

def put_in(qus,ans):#new entry 
    c.execute("INSERT INTO entries VALUES('{}','new','{}')".format(qus,ans))
    con.commit()


def ask_qus(qus):#asking qustions
    print("Let me ask the same thing from you :")
    print(qus)
    ans=input(">")
    put_in(qus,ans)
    print("oka")
    



def user_input():#input
    qus=input(">")
    if qus=='bye' or qus=='exit' or qus=='exit':
        return False
    
    if len(qus.split()) <4:
        third=qus.split()
        for i in range(0,len(third)):
         ans=find_qus(third[i])
         if ans:
            print(">",third[i]," ->>")
            for a in ans:
                print(a)
        print(">>And I hate short sentences ! ")
    else:
        ans=find_qus(qus)
        if ans :
           print(">",ans)
        else :
           print(">I Don't Know This...But I Knew This ->>")
           third=qus.split()
           for i in range(0,len(third)):
             ans=find_qus(third[i])
             if ans:
               print(">",third[i]," ->>")
               for a in ans:
                print(a)  

           ask_qus(qus)
    return True
#main
print("WELCOME ")
condition=True
while(condition):
    condition=user_input()

print("Thankyou and have nice day")
#end
######BINI#######BINI######BINI########BINI########BINI#######BINI#######BINI#####    
