blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#	
height = 0
steps = 0

while steps < blocks:
    height += 1
    blocks -= steps
    steps += 1

print("The height of the pyramid:", height)
