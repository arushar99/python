#Name:Arusha Herath
#Course:
#Date:
#
#Analysis
#Input:string/file
#Outputs:a encrypted/decrypted string or file
#
#
#Method/Algorithm:
#Step 1:Start
#Step 2:make the defualtkey = 'qwertyuiopasdfghjklzxcvbnm' a global varaible
#Step 3:make a string contaning all the lower letters in the alphabet
#Step 4:make a string contaning all the upper letters in the alphabet
#Step 5:defined a menu function with no parameter
#       Step 5a:print("Welcome to Arusha's Encryption & Decryption Program")
#       Step 5b:print("===================================================")
#       Step 5c:print()

#       Step 5d:print("How Can We Help You Today")
#       Step 5e:print("=========================")
#       Step 5f:print()
#       Step 5g:print("1. Encrypt a String using default Key")
#       Step 5h:print("2. Encrypt a String using your own Key")
#       Step 5i:print("3. Decrpyt a String using default Key")
#       Step 5j:print("4. Decrypt a String using your own Key")
#       Step 5k:print()
#       Step 5l:print("5. Encrypt a file using your own Key")
#       Step 5m:print("6. Decrypt a file using your own Key")
#       Step 5n:print("7. Encrypt a file using default Key")
#       Step 5o:print("8. Decrypt a file using default Key")
#Step 6:Defined a function called StrEncrypt(string,key) with two parameters
#       Step 6a:make an emtpy string and set strEncrypted equal to that
#       Step 6b:using a for loop, iterate through every character in the string
#               Step 6b I:if char in upperLetters:
#                       Step 6b I a:let index equal to the index of the char in the string containing upperletters.
#                       Step 6b I b:let upper equal to the key[index] and make it upper case after
#                       Step 6b I c:then added it to the empty string( strEncrypted)
#               Step 6b II:if char in lowerLetters:
#                       Step 6b II a:let index equal to the index of the char in the string contaning lowerletters.
#                       Step 6b II b:let lower equal to the key[index]
#                       Step 6b II c:add it to the empty string(strEncrypted)
#               Step 6b IIIL:if it doesn't go in other two
#                       Step 6b III a: add it to the empty string(strEncrypted)
#       Step 6c:return strEncrypted
#Step 7:Define a function called StrDecrypted(string,key) with two parameters
#       Step 7a:make an empty string and set strDecrpted eqaul to that
#       Step 7b:using a for loop, iterate thorugh every character in the string
#               Step 7b I:if char in upperLetters:
#                       Step 7b I a:make the char a lowercase first
#                       Step 7b I b:let index equal to the key.index(char)
#                       Step 7b I c:upper equal to the upperLetters[index]
#                       Step tb I d:add it to the empty string(strDecrypted)
#               Step 7b II: if char in lowerLetters:
#                       Step 7b II a:let index equal to the key.index(char)
#                       Step 7b II b:lower equal to the lowerLetters[index]
#                       Step 7b II c:add it to the empty string(strDecrypted)
#               Step 7b III:else:
#                       Step 7b III a:add it to the empty string(strDecrypted)
#       Step 7c:return strDecrytped
#Step 8:Define a function called encryprFileOwnKey( InputFile, ownKey, OutputFile):
#       Step 8a:using a for loop iterate through each line in the file
#                       Step 8a I:let EncryptLine equal to the strEncrypt( line, ownKey)
#                       Step 8a II:write the EncryptLine to the output file after
#Step 9:Define a function called decryptFileOwnKey( InputFile, ownKey, OutputFile);
#       Step 9a:using a for loop iterate throguh each line in the file
#                       Step 9a I:let DecryptLine = strDecrypt(line, ownKey)
#                       Step 9a II:write the DecryptLine to the output file after
#Step 10:Define a function called decryptFileDefaultKey( InputFile , OutputFile)
#       Step 10a:using for loop iterate through each line in the file
#                       Step 10a I:let DecryptLine equal to the strDecrypt(line, defaultKey)
#                       Step 10a II:write the DecryptLine to the output file after
#Step 11:Define a function called encryptFileDefaultKey (InputFile, OutputFile)
#       Step 11a:using a for loop iterate through each line in the file
#                       Step 11a I:let EncryptLine equal to the StrEncrypt(line, defaultKey)
#                       Step 11a II:write the EncryptLine to the output file after
#Step 12:Define a main function with no parameters
#       Step 12a:call the menu function [ menu() ]
#       Step 12b:let InputFile = KeyFile = OutputFile = None
#       Step 12c:files=[InputFile, KeyFile, OutputFile]
#       Step 12d:Using a while loop with True as the condition
#                       Step 12d I:using try and exception. under try, let user_input equals to the user input
#                       Step 12d II:if user_input is in between 1 and 8 then break out of the while loop
#                       Step 12d III:else, go to the except ValueError, print("Oops, Try again") go back and ask for user's input
#       Step 12e:if user_input in [5,7]
#                       Step 12e I:using a while loop with True as the condition
#                                   Step 12e I a:ask user for input file and set InputName equals to that
#                                   Step 12e I b:using try and exceptions, under try, try to open the file using r mode, if it exists, break out of the while loop
#                                   Step 12e I c:if the file doesn't exist go to the except IOError, and print("FIle doesn't exists") then go back up and ask for a input again
#       Step 12f:if user_input in [6,8]
#                       Step 12f I:using a while loop with True as the condition 
#                                   Step 12f I a:ask user for input file and set InputName equals to that
#                                   Step 12f I b:using try and exceptions, under try, try to open the file using r mode, if it exists, break out of the while loop
#                                   Step 12f I c:if the file doesn't exist go to the except IOError, and print("FIle doesn't exists") then go back up and ask for a input again
#       Step 12g:if user_input is in [2, 4, 5, 6]
#                       Step 12g I:using a while loop with True as the condition
#                                   Step 12g I a:ask ser for a Key file and let it equal to KeyName
#                                   Step 12g I b:using try and exception, under try, try opening the file with r mode
#                                   Step 12g I c:if the file exist let ownKey equals to Keyfile.read meaning read the first line only
#                                   Step 12g I d:if it doesn't exists then, go to except IOError and print it odesn;t exists and go back up to the top of the loop and ask for use to enter the correct key file
#       Step 12h:if user_input in the [5,7]
#                       Step 12h I:using a while loop with True as the condition
#                                   Step 12h I a:ask user for an outputfile and let it equals to OutputName
#                                   Step 12h I b:using try and exception, try opening the file with x mode, if the file doesn't already exists then break out of the while loop
#                                   Step 12h I c:if it already exists, go to excepion, if the output name equals the inputname, print a message and ask for a new output name
#                                   Step 12h I d:if the output name equals the key name and user's input == 5, print a message and ask for a new output name
#                                   Step 12h I e:if the file already exsit , then ask for user's permission to append to it
#                                   Step 12h I f:if user enter YES then append to that file else, ask for a new output file name
#       Step 12i:if user_input in [6,8]
#                       Step 12i I:using a whle loop with True as the condition
#                                   Step 12i I a:ask user for an output file name, and set it equals to OutputName
#                                   Step 12i I b:using try and exception,try opening the file with x mode, if the file doesn't already exists, then break out of the while loop
#                                   Step 12i I c:if the file already exists, then go to exception, if the OutputName equals to the Inputname,print a mseeagge and ask for a new OutputName
#                                   Step 12i I d:if the OutputName equals the KeyName, print a message and aks for new OutputName
#                                   Step 12i I e:if the file already, then ask for user's permission to append to it
#                                   Step 12i I f:if user enter YES then append to that file ,else ask fri a new output file name
#       Step 12j:if user_input in [1,3,7,8]
#                       Step 12j I;print a message letting the yuser know that they will be using the default key to encrypt/decrypt
#       Step 12k:if user_input == 1
#                       Step 12k I:ask user for a string
#                       Step 12k II:call the strEncrypt function with (user_str, defaultKey) as the arguments and let defaultEncryption variable equal to that
#                       Srep 12k III:print(defaultEncryption)
#       Step 12l:if user_input == 2
#                       Step 12l I:ask user for a string
#                       Step 12l II:call the strEncrypt function with (user_str, ownKey) as the arugements and let it equal to strEncryption variable
#                       Step 12l III:print(strEncryption)
#       Step 12m if user_input == 3
#                       Step 12m I:aks user for a string (encrypted)
#                       Step 12m II:call the strDecrypt function with (user_str, defaultKey) as the arguments and let it equal to DefaultStrDecryption
#                       Step 12m III:print(DefaultStrDecryption)
#       Step 12n:if user_input == 4
#                       Step 12n I:ask user for a strin (encrypted)
#                       Step 12n II:call the strDecrypt function with (user_str, ownKey) as the arguments and let it equal to StrDecryption
#                       Step 12n III:print(StrDecryption)
#       Step 12o:if user_input == 5
#                       Step 12o I:call the functon encryptFileOwnKey with (InputFile, ownKey, OutputFile) as the arguments
#       Step 12p:if user_input == 6
#                       Step 12p I:call the function decryptFileOwnKey with (InputFile, ownKey, OutputFil) as the arugments
#       Step 12q:if user_input == 7
#                       Step 12q I:call the function encryptFileDefaultKey woth (InputFile, OutputFile) as the arugments
#       Step 12r:if user_input == 8
#                       Step 12r I:call the function decryptFileDefaultKey with (InputFile, OutputFile) as the aruguments
#       Step 12s:using a for loop iterate through each file in the files, and if file is not None, then close the file
#Step 13:Close the main




#TestCases:1
#Input:Welcome to Arusha's Encryption & Decryption Program
##===================================================
##
##How Can We Help You Today
##=========================
##
##1. Encrypt a String using default Key
##2. Encrypt a String using your own Key
##3. Decrpyt a String using default Key
##4. Decrypt a String using your own Key
##
##5. Encrypt a file using your own Key
##6. Decrypt a file using your own Key
##7. Encrypt a file using default Key
##8. Decrypt a file using default Key
##
##Please select an option from the selection: 1
##
##****Note: We Will be using the default key to encrypt your code*****
##
##Please enter the string you want to encrypt: I love lolipop
##

#Expected OutPut:
#O sgct sgsohgh
#

#TestCase:2
#Input:
##Welcome to Arusha's Encryption & Decryption Program
##===================================================
##
##How Can We Help You Today
##=========================
##
##1. Encrypt a String using default Key
##2. Encrypt a String using your own Key
##3. Decrpyt a String using default Key
##4. Decrypt a String using your own Key
##
##5. Encrypt a file using your own Key
##6. Decrypt a file using your own Key
##7. Encrypt a file using default Key
##8. Decrypt a file using default Key
##
##Please select an option from the selection: 3
##
##****Note: We Will be using the default key to encrypt your code*****
##
##Please enter the string you want to decrypt: O sgct sgsohgh

#Expected Output:
#I love lolipop

#Program:

defaultKey = 'qwertyuiopasdfghjklzxcvbnm'    # make all of these string a global varaible 
lowerLetters = 'abcdefghijklmnopqrstuvwxyz'
upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#######################################################################################

def menu():

    print("Welcome to Arusha's Encryption & Decryption Program")
    print("===================================================")
    print()

    print("How Can We Help You Today")
    print("=========================")
    print()
    print("1. Encrypt a String using default Key")
    print("2. Encrypt a String using your own Key")
    print("3. Decrpyt a String using default Key")
    print("4. Decrypt a String using your own Key")
    print()
    print("5. Encrypt a file using your own Key")
    print("6. Decrypt a file using your own Key")
    print("7. Encrypt a file using default Key")
    print("8. Decrypt a file using default Key")

#########################################################################################    

 

def strEncrypt(string,key):
    


    strEncrypted = ''
    
    for char in string:

        if char in upperLetters: #if char is in upperLetters
            

            index = upperLetters.index(char) #check for the index in the upperLetters string
            upper = key[index].upper()#find the character for that index in the key
            strEncrypted += upper #add it to the empty string

        elif char in lowerLetters: #if char is in lowerLetters

            index = lowerLetters.index(char) #check for the index in the lowerLetters string
            lower = key[index] #find the character for that index in the key
            strEncrypted += lower #add it to the empty string

        else:
            strEncrypted += char #if it's an special character, keep it the same and add it to the empty string
    return strEncrypted
######################################################################################

def strDecrypt(string,key):
 
    strDecrypted= '' #make an empty string
    
    for char in string: #go thru each character in the string 

        if char in upperLetters: #if the charatcer is an upper case letter
            char = char.lower() #make it a lower case

            index = key.index(char) #check for the index in the key
            upper = upperLetters[index] #find the character for the same index in the upperLetters string
            strDecrypted += upper #add to the empty string

        elif char in lowerLetters: #if the character is a lower case letter

            index = key.index(char) #check for the index in the key 
            lower = lowerLetters[index] #find the charatcer for that index in the lowercase letters string
            strDecrypted += lower #add to the empty string

        else: #if it's other than a upper case or a lower case letter don't change anything 

            strDecrypted += char #add to the empty string

    return strDecrypted
####################################################################################

def encryptFileOwnKey(InputFile, ownKey, OutputFile):
    
    for line in InputFile: #go thru line by line in the file

        EncryptLine = strEncrypt(line,ownKey) #call the strEncrypt function each time

        OutputFile.write(EncryptLine) #write it to the output file each time


    
#####################################################################################
        
def decryptFileOwnKey(InputFile, ownKey, OutputFile):
    for line in InputFile:

        DecryptLine = strDecrypt(line,ownKey) #call the strDecrypt function each time

        OutputFile.write(DecryptLine) #write to the output file each time
    
#######################################################################################
        
def decryptFileDefaultKey(InputFile, OutputFile):
        for line in InputFile:

            DecryptLine = strDecrypt(line,defaultKey) #call the strDecrypt function each time

            OutputFile.write(DecryptLine)   #write to the output file each time
            
######################################################################################
            
def encryptFileDefaultKey(InputFile, OutputFile):
    for line in InputFile:

        EncryptLine = strEncrypt(line,defaultKey)  #call the strEncrypt function each time

        OutputFile.write(EncryptLine) #write to the output file each time
            
        

            
#########################################################################################  
def main():
    menu()
    print()
    
    InputFile = KeyFile = OutputFile = None
    files = [InputFile, KeyFile, OutputFile]
        
    while True:
        try:
            user_input = int(input("Please select an option from the selection: "))
            if 1<= user_input<= 8:
                break
        except ValueError:
            print("Oops!! Try Again!")

    if user_input in [5,7] :
        while True:
            InputName = input("Please enter the InputFile name: ")
            try:
                InputFile = open(InputName,'r')
                break
            except IOError:
                print("The file",InputName,"doesn't exists")
    if user_input in [6,8]:

        while True:
            InputName = input("Please insert the InputFile name: ")
            try:
                InputFile = open(InputName,'r')
                break
            except IOError: #to check if user enter the correct file name if not keep asking the user
                print("The file",InputName,"doesn't exist")
        
                
    if user_input in [2,4,5,6]: #only go in here for one's where user wants to use their own key
        
        while True:
            KeyName = input("Please enter the KeyFile name: ")

            try:
                KeyFile = open(KeyName,'r') #to keep asking for the right key file if it doesn't exist
                ownKey = KeyFile.readline()  # the first line which contains the key
                break
            except IOError:
                    
                    print("The file",KeyName,"doesn't exists")

    if user_input in [5,7]:  #only go in here if user's want to encrypt/decrypt a file into a output

        while True:
            OutputName = input("Please enter the OutputFile name: ") 
            try:
                OutputFile = open(OutputName,'x')#to make sure the file exist
                break
            except IOError:
                
                if OutputName == InputName: # if it equals the input name 
                    print("It's same as Input file")
                    continue 
                if user_input == 5 and OutputName == KeyName:
                    print("It's same as Key file")# if it equals the key name
                    continue 

                ask_user = input("Do you want to append to this file(YES/NO): ")
                if ask_user == "YES":
                    OutputFile = open(OutputName,'a')
                    break
                    
    if user_input in [6,8]:
        while True:
            
            OutputName = input("Please enter the OutputFile name: ")
            
            try:

                OutputFile = open(OutputName,'x') #to make sure the file exist
                break
            
            except IOError:
                
                if OutputName == InputName:
                    print("It's same as Encrypted file!")
                    continue
                
                if OutputName == KeyName:
                    print("It's same as Key file!")# if it equals the key name
                    continue 

                ask_user = input("Do you want to append to this file(YES/NO): ")
                if ask_user == "YES":
                    OutputFile = open(OutputName,'a')
                    break      

    
    if user_input in [1,3,7,8]: #only for these value it will show this note
        print()
        print("****Note: We Will be using the default key to encrypt/decrypt your code*****")
        print()
      

    if user_input == 1: #to use default key to encrypt a string
        
        user_str = input("Please enter the string you want to encrypt: ")
        defaultstrEncryption = strEncrypt(user_str,defaultKey)
        
        print(defaultstrEncryption)

    if user_input == 2: #to use user's key to encrypt a string 
        user_str= input("Please enter the string you want to encrypt:")
        strEncryption = strEncrypt(user_str,ownKey)

        print(strEncryption)

    if user_input == 3:#to use default key to decrypt a string

        user_str = input("Please enter the string you want to decrypt: ")
        DefaultStrDecryption = strDecrypt(user_str,defaultKey)

        print(DefaultStrDecryption)

    if user_input == 4: #to use user's key to decrypt a string

        user_str = input("Please enter the string you want to decrypt: ")
        StrDecryption = strDecrypt(user_str,ownKey)

        print(StrDecryption)


    if user_input == 5: #to encrypt using own key 

        encryptFileOwnKey(InputFile, ownKey, OutputFile)  

    if user_input == 6: #to decrypt using own key
        
        decryptFileOwnKey(InputFile, ownKey, OutputFile)

    if user_input == 7:  #to encrypt using default key
        encryptFileDefaultKey(InputFile, OutputFile)    

    if user_input == 8:  #to decrypt using default key
        
        decryptFileDefaultKey(InputFile, OutputFile)

    for file in files:
        if file is not None: #to close the files that we've opened
            file.close()
        
main()

