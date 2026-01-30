import re

# text = "Pyhton in powerful"
# res = re.search("powerful",text)
# if res :
#     print("Match found:", res.group)

text = "my number is 1234567890 and 1234567890"

for match in re.finditer("\d{10}",text):
    print("Match found at index:",match.start(),"to",match.end())

print("")