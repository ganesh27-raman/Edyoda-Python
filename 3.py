def areRotations(string1, string2):
    num1 = len(str1)
    num2 = len(str2)
    temp = ''

    if num1 != num2:
        return 0
 
    temp = str1 + str1
    
    if (temp.count(str2)> 0):
        return 1
    else:
        return 0

str1 = "AACD"
str2 = "ACDA"
 
if areRotations(str1, str2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")