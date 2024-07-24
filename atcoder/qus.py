# s="kopalgangrade"
# c=0
# for i in range(len(s)):
#   for j in range(len(s)):
#     if s[i]==s[j+1]:
#       c+=1
#     print(c)



# Given string
S = "HellO"

# Check if the first character is uppercase and all other characters are lowercase
if 'A' <= S[0] <= 'Z' and all('a' <= char <= 'z' for char in S[1:]):
    print("Condition is satisfied")
else:
    print("Condition is not satisfied")
