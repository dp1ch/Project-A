import random
import local
def RefreshWord(picked,word,secret):
    
    for i in range(len(word)):
        result=""
        F=0
        if secret[i]==picked:
            word[i]=picked
            F+=1
    if F>1:
        print(local.UFIND,F,local.LETTERS)
    for i in word:
    	result+=str(i)
    print(result)
    print(tries)
    return word
    

Sport=local.SPORT
Transport=local.TRANSPORT
Biology=local.BIOLOGY
Politics=local.POLITICS
Geography=local.GEOGRAPHY
def Generate():
    a=input(local.CHOOSE).lower()
    category="Политика"
    if a =="с":
        category="Спорт"
        pull=Sport
    elif a == "т":
        category="Транспорт"
        pull=Transport
    elif a=="б":
        category="Биология"
        pull=Biology
    elif a=="п":
        category="Политика"
        pull=Politics
    elif a=="г":
        category="География"
        
        pull=Geography
    else:
        category="Биология"
        pull=Biology
    secret=pull[random.randint(0,len(pull)-1)].lower()
    return secret,pull,category
secret,pull,category=Generate()
tries=5
word=[]
ban={',','*','&','.','!','1','2','3','4','5','6','7','8','9','?','%',':',';','$','#','№'}
flag=True
print(local.START1,tries,local.START2,category,local.SIGN)
for i in (secret):
    word.append("*")
word=RefreshWord(' ',word,secret)
while tries!=0:
    if '*' not in word:
        print(local.WON)
        if input(local.RESTART) =="р":
            secret,pull,category=Generate()
            tries=5
            word=[]
            for i in (secret):
                word.append("*")
            flag=True
            continue
    if flag==True:
	    flag=False
	    result=""
	    for i2 in word:
	    	  result+=str(i2)
	    print(result)
    picked=input(local.CHOOSELETTER).lower()
    
    if len(picked)>1 or picked in ban:
        print(local.PROHIBITED)
        
    if picked in secret:
        print(local.SCORED)
        word=RefreshWord(picked,word,secret)
        continue
    print(local.NOTSCORED)
    tries-=1
    print(tries)
if tries==0:
    print(local.FINAL,secret)
    
