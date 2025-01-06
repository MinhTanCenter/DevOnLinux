ss = int(input("Enter seconds: "))
s = ss % 60
m = ss//60%60
h = ss//3600%34
d = ss//(60*60*24)
print(d,"days", m, "minutes", s, "seconds")