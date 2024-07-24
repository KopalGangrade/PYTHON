t=int(input())
for _ in range(t):
    N=int(input())
    S=input()
    if(N<8):
        print(8-N)
    else:
        l=[0,0,0]
        for i in S:
            if i.isupper()==True:
                l[0]=1
            if i.islower():
                l[1]=1
            if not i.isalpha():
                l[2]=1
        if(sum(l)==3):
            print(0)
        else:
            print(3-sum(l))