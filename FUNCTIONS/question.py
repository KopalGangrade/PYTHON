# s=input()
# n=len(s)
# for i in range(n):
#     if s[i]!="@":
#         print(" ")
#     else:
        # print()

# s="abc@xyz.com"
# m=s.split('@')
# print(m)
# st=m[1]
# d=st.split(".com")
# print(d)



# call by refrence

def abc(a):
    a[2]=78
    return a
b=[1,2,3,4,5]
abc(b)
print(b)

#call by value

def abc(a):
    a="hello kopal"
    return a
b="hello"
abc(b)
print(b)
    