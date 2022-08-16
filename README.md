# greykey_password_extractor
 
1) This script extract passwords from the text document created when conducting a greykey extraction.
2) These text files often are named as such: [8 numbers]-[15 numbers][passwords].txt. 
3) Place this script in the same directory as that password text document. 
4) Run this script in a command line. The only argument should be the name of the text document. 
5) This script will use regex to remove all unrequired text from the document, and place each password on a new line. 
6) The output text document will keep the original filename, with "Extracted passwords from - " prefixed, so you know where the results are from. 