import os

#you must have docx2pdf installed 
#must have libreoffice installed 

#the security is a bit iffy 

filename = ''  #file to be converted 
os.system("soffice --convert-to pdf "+filename+".docx")


#send file back to the user 