try:
	from PIL import Image,ImageFilter,ImageEnhance 
except ImportError:
    import Image
import pytesseract
#import Image

#Read image
im = Image.open('page_1.jpg')
#Display image  
#im.show()
   
enh = ImageEnhance.Contrast(im)  
enh = ImageEnhance.Brightness(im)
im = enh.enhance(1.2)

im.save('outer.jpg')

'''
Part #2 - Recognizing text from the images using OCR
'''
	#3
# Variable to get count of total number of pages


# Creating a text file to write the output
outfile = "OCRtext/test.txt"

# Open the file in append mode so that
# All contents of all images are added to the same file
f = open(outfile, "a")

# Iterate from 1 to total number of pages
for i in range(1, 2):

	# Set filename to recognize text from
	# Again, these files will be:
	# page_1.jpg
	# page_2.jpg
	# ....
	# page_n.jpg
	filename = "page_"+str(i)+".jpg"
		
	# Recognize the text as string in image using pytesserct
	text = str(((pytesseract.image_to_string(Image.open('outer.jpg'), lang='eng+ara'))))

	# The recognized text is stored in variable text
	# Any string processing may be applied on text
	# Here, basic formatting has been done:
	# In many PDFs, at line ending, if a word can't
	# be written fully, a 'hyphen' is added.
	# The rest of the word is written in the next line
	# Eg: This is a sample text this word here GeeksF-
	# orGeeks is half on first line, remaining on next.
	# To remove this, we replace every '-\n' to ''.
	text = text.replace('-\n', '')	

	# Finally, write the processed text to the file.
	f.write(text)

# Close the file after writing all the text.
f.close()



