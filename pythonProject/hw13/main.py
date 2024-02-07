with open('example.txt', 'w') as file:
   for i in range(1,1001):
       file.write(f"{i}: texti\n")
with open('example.txt', 'r') as file:
    reader = file.read()

    print(reader)