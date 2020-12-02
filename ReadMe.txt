Name: Krishna Mani arasu	
Programming language: Python 3.8.5
Compiler: MSC v.1926 32 bit (Intel)
Algorithm: Lempel Ziv Welch (Lempel Ziv Coding)
Files: Lempel.py, plain.txt, Encoded.txt, Decoded.txt

This python program "Lempel.py" helps you to simulate the Lempel ziv coding

Before running the program:
	1) Create plain.txt file or the text file you need to encode
        2) Keep the text file in the same location as the python file

How to run the file:
	1) Open the command prompt window
        2) Go the file directory, where your text and python file located [For Help, see this website: "https://www.onmsft.com/feature/command-prompt-basics-working-with-files-and-folders"]
	3) After reaching the location, type: "python Lempel.py"

This "Lempel.py" program encodes the given plain text file and store it in the newly created file "Encoded.txt" and again it decodes and store it in the newly created file "Decoded.txt"

Encoding:
	First, it will create a dictionary of size 256, which contains characters and ascii values as their keys and values.
        Then the data is read from the plain text file one by one and added to the dictionary only if that data is not in the dictionary.
        Encoded data is printed on the command prompt and separate file ("Encoded.txt") is created in the same location as plain text file.

Decoding:
        Same as Encoding, First it will create a dictionary of size 256.
	But here ascii values and characters are keys and values.
	Note: ascii values and characters are interchanged from encoding dictionary.
	Then each value is read from the encodedData and try to find the corresponding characters. 
	In some cases, while reading the values from encodedData, that values can not be found in the intial dictionary.
	So we add the values in the dictionary for the combination of data already read from encodedData. 
	Decoded data is printed on the command prompt and separate file (Decoded.txt) is created in the same location as Encoded text file.
	 

 
