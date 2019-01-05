import json

# jsonFile = open("finalJson.json", "r") # Open the JSON file for reading
# data = json.load(jsonFile) # Read the JSON into the buffer
# keys =  data.keys()
# print (keys)
#
#    ## Working with buffered content
# for i in range(len(data)):
#    if 'created_at' in data:
#        print (data[i]['created_at'])


jsonFile = open("finalJson.json", "r")
tweetObj = json.load(jsonFile)
print(tweetObj)
keys = tweetObj.keys()
print(keys)
for line in jsonFile:
    if 'text' in tweetObj:
        print(tweetObj['text'])
    else:
        print('This does not have a text entry')
