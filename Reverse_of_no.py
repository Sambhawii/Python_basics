Num=int(input("enter your no to reverse"))
reverse=0;

while(Num>0):
    remender=Num%10;
    reverse=(reverse*10)+remender;
    Num=Num//10;
print(reverse)



