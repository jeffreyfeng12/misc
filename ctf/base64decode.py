import base64

with open('weird.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
    
    data = base64.b64decode(data)

print data