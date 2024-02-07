def addit(a,b):
    return a+b

with open ("example.txt", 'w') as file:
    file.write("ahdvahfajbfiaufafaf"
               "akjfaoipfjafnakjfn"
               "afksbaskjfasfasf"
               "akfhasfhaskjf")
with open ("example.txt", 'r') as file:
    x = file.read()
with open ("example1.txt", 'w') as file:
    file.write("13214263431"
               "1`24363124345"
               "1235463124354")
with open ("example1.txt", 'r') as file:
    y = file.read()
print(addit(x,y))