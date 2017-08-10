#1.
OUTPUT_FILE = "Name"
out_file = open(OUTPUT_FILE, 'w')
Name = input("Input Name")
print(Name, file=out_file)
out_file.close()

#2.
in_file = open("Name", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

#3.
in_file = open("Numbers","r")
total = 0
for line in in_file:
 number = int(line)
 total += number
print(total)
in_file.close()




