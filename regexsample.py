import re

txt = "The rain in Spain"
match = re.search("^The.*Spain$", txt)  # Returns a Match object if there is a match anywhere in the string
print(match.string)

results = re.findall("[\\w]*in", txt)  # Returns a list containing all matches

for result in results:
    print(result)

# https://www.w3schools.com/python/python_regex.asp
