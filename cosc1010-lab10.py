# Jared Tolman
# UWYO COSC 1010
# Nov 20th, 2024
# Lab 10
# Lab Section: 15
# Sources, people worked with, help given to: Some Google searches were made for function and syntax help.
# 

#import modules you will need 

from hashlib import sha256 
def get_hash(to_hash):
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.

# - Read in the value stored within `hash`.
#   - You must use a try and except block.

try:
    with open("hash", "r") as pwhash:
        hash=pwhash.read().strip()
except FileNotFoundError:
    print(f"Could not find the file named 'hash'")
    exit()
except Exception as Error:
    print(f"The following error occurred for 'hash': {Error}")
    exit()

# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

try:
    with open("rockyou.txt", "r") as rockyoulist:
        rockyou=rockyoulist.readlines()
except FileNotFoundError:
    print(f"Could not find the file named 'rockyou.txt'")
    exit()
except Exception as Error:
    print(f"The following error occurred for 'rockyou.txt': {Error}")
    exit()
else:
    for pw in rockyou:
        pw=pw.strip()
        if get_hash(pw)==hash:
            print(f"The cracked password is '{pw}'")
            break
    else:
        print("The correct password could not be found")