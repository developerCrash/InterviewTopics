## Reads entire file 
with open("anil.txt", "r") as f:
    content = f.read()
    print(content)


## Read Line by line
with open("anil.txt", "r") as f:
    for line in f:
        print(line.strip())

## Read line by line in a list 
with open('anil.txt', 'r') as file:
    lines = f.readlines()
    print(lines)

## Reading Characters 
with open('anil.txt', 'r') as f:
    content = f.read(10)  # Reads the first 10 characters
    print(content)
    print(f.tell())  # Get the current position (should be 0 initially)
    f.seek(0)  # Move back to the start of the file


lines = ["First line\n", "Second line\n", "Third line\n"]

# Open the file in write mode
with open('example.txt', 'w') as file:
    file.writelines(lines)
    file.flush()  # Flushes the internal buffer to disk
