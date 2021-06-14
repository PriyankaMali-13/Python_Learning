import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")


#findall()
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#split()
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Replace every white-space character with the number 9
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


#Search for an upper case "S" character in the beginning of a word, and print its position
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Search for an upper case "S" character in the beginning of a word, and print the word
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())