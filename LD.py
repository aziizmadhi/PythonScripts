from langdetect import detect



myfile = open('test.txt')
mytxt = myfile.read()

lang = detect('mytxt')

print (lang)

myfile.close()

