first =int(input("enter the first number"))
second=int(input("enter the second number"))
temp1=first;
temp2=second;
while (temp2 != 0):
            temp = temp2;
            temp2 = temp1 % temp2;
            temp1 = temp;
        

hcf = temp1;
lcm = (first* second) / hcf;
print(hcf);
print(lcm);
