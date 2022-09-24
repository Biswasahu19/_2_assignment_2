my_dict = dict()

start = int(input("Enter the start of ascii range: "))

end = int(input("Enter the end of ascii range: "))

for i in range(start, end):

   my_dict [chr(i)] = str(i)

print(my_dict)

