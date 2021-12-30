def new_string(str):
    d={"UpperCase":0, "LowerCase":0}
    for i in str:
        if i.isupper():
            d["UpperCase"]+=1
        elif i.islower():
            d["LowerCase"]+=1
        else:
            pass
    print("Original String", str)
    print("No. of Upper Case Character : ", d["UpperCase"])
    print("No. of Lower Case Character : ", d["LowerCase"])
new_string('The quick Brow Fox')