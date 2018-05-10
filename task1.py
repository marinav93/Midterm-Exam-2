"""
===================   TASK 1   ====================
* Name: Caesar Cipher
*
* Caesar Cipher is encryption technique in which
* each letter in the plaintext is replaced by a
* letter some fixed number of positions down the
* alphabet. The method is named after Julius Caesar,
* who used it in his private correspondence.
*
* Write a script that will accept number of positions
* that should be shifted down the Unicode code points
* of character. White spaces and punctuation marks
* should be ignored during encryption process.
*
* Hint: `ord()` returns integer representing Unicode
* code point for single character.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

inp = input('Input the text you want to code:\n')
inp = inp.lower()

key = int(input('Input the key you want to use from 2 to 25:\n'))
def rot13(input,key): #Function to code a text with caeser chyper.
    if key > 25:
        key = 25
    elif key < 2:
        key = 2
    finaltext = ''
    for letter in input:
        if letter.isalpha():
            num = ord(letter)
            if (num + key) > 122: #If the final number is greater than 122..
                x = (num + key) - 122
                finaltext += chr(x + ord('a') - 1)
            elif((num + key <= 122)):
                finaltext += chr(num + key)
        else:
            finaltext += letter
    print(finaltext)


rot13(inp,key)


# Write your functions here



def main():
    # Test your functions here
    pass

if __name__ == "__main__":
    main()