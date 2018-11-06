import urllib.request
file = urllib.request.urlopen('http://helloworldbook2.com/data/message.txt')
message=file.read()
print(message)
