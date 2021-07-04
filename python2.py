#Part 1

#print("\n")

#QUESTION 1

#import string

#str_of_user = input('Enter any string of letters: ')

#if str_of_user.isnumeric():
    #raise Exception("string of letters does not contain letters")


#set_of_user = set(str_of_user.lower())
#alphabet = set(string.ascii_lowercase)

#print("Letters not used:", "".join(sorted(list(alphabet.difference(set_of_user)))))

#print("\n")

#Part 2

#print("\n")

#QUESTION 3

#string = input("Enter any string: ")

#if string == 'x':
    #exit()
#else:
    #newstr = string
    #print("\nRemoving vowels from the given string")
    #vowels = ('a', 'e', 'i', 'o', 'u')
    #for x in string.lower():
        #if x in vowels:
            #newstr = newstr.replace(x,"")
    #print("New string after successfully removed all the vowels:")
    #print(newstr)

#print("\n")

#QUESTION 4

#def is_string(input_str):
    #if input_str.strip().isdigit():
        #print(f"The input value {input_str}  'int'")
    #elif input_str.replace(".","").isnumeric():
        #s = float(input_str)
        #print(f"The input value {input_str}  'float'")
    #else:
        #print(f"The input value {input_str}  'string'")


#str1 = input("Enter string and hit enter :")
#is_string(str1)

#str2 = input("Enter string and hit enter :")
#is_string(str2)
