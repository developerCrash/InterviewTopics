import re

pattern = re.compile(r'aa')
replacement_string = 'bb'

myStr = "Anil kumar is aa witaa apple"

result = pattern.findall(myStr)
print(result if result else "NO Match")
## Print the number of times a substring is repeated 
print(len(result))

result = pattern.sub(replacement_string, myStr)
print(result)
