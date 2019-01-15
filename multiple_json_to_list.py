import json
import re

# with open("tweets_text.txt", "r") as file:
#     myJson = file.read()
#
#
# myJson = myJson.replace("} {", "}###{")
# print("after replace: ", myJson)
# new_list = myJson.split('###')
# print("after split: ",new_list)
# new_list = new_list.replace('\r\n', '\r,')
# print("end", new_list)


with open("tweets.txt") as f:
    content = f.read().splitlines()

print(content)
