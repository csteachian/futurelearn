# Create a function that accepts a
# string and returns the same string 
# reversed.

def reverseme(input):
  output = ""
  for index in range(len(input)-1,-1,-1):
    output = output + input[index]
  return output

thisinput = input("Enter a string to be reversed: ")
print(reverseme(thisinput))
