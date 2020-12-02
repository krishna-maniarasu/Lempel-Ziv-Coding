
#####  Encrpytion #########
from struct import *
filename="plain.txt"
fileHandle=open(filename,"r")
data=fileHandle.read()
print("DATA:\n",data,end="\n")
CompressedData=[]
rootPart=''

# Intial dictionary creation #
dictionary={chr(i):i for i in range(256)}
size=256

#  Checking with dictionary
print("\nAdding new values in dictionary")
for inputSymbol in data:  #Getting new inputSymbol from file
    value=rootPart+inputSymbol
    if value in dictionary:  #Checking whether the data is in dictionary
        rootPart=value   #Content is in the dictionary, So keeping the data for next iteration
    else:
       addPart=dictionary.get(rootPart,45)
       CompressedData.append(addPart)  #Transmit the present address
       dictionary[value]=size  # Add the new value to the dictionary
       print(value,"\t",size,end="\n")
       size+=1
       rootPart=inputSymbol #Changing the starting point of the rootPart to the current inputSymbol

#Checking the last letter in the file
if rootPart in dictionary:
    CompressedData.append(dictionary[rootPart])

print("Encoded data:\n",CompressedData,end="\n")
output_file = open("Encoded.txt", "w")
for data in CompressedData:
    data=str(data)
    data=data+","
    output_file.write(data)
output_file.close()
fileHandle.close()



########   Decryption   ###############
decodedData=[]
string=""
Dsize=256
print("\nCreating dictionary for Decryption",end="\n")
Decryption_dictionary={i:chr(i) for i in range(256)}
for value in CompressedData:
    if not(value in Decryption_dictionary):
        Decryption_dictionary[value]=string+string[0]
    decodedData+=Decryption_dictionary[value]
    if (len(string)!=0):
        Decryption_dictionary[Dsize]=string+(Decryption_dictionary[value][0])
        Dsize+=1
    string=Decryption_dictionary[value]


for data in decodedData:
    print(data,end="")
decodedfile = open("Decoded.txt", "w")
for data in decodedData:
    data=str(data)
    decodedfile.write(data)
decodedfile.close()
