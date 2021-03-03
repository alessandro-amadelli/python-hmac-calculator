# -*- coding: utf-8 -*-
#
"""
This script let you generate an HMAC keyed hash for a file by inserting filename and hash key.
You can also compare the newly generated hash with an old one for the same file to tell if they are different.

This is useful if you want to be sure that no one modified the file since the last time you checked it.

Instruction:
1_Create a file (or take an existing one)
2_Run the script inserting file name and choosing a password (key)
3_Save the generated hash
4_Next time you want to check the file you just have to run the program again (2) inserting the key you chose the previous time
5_After the program calculates hash, choose option "C"
6_Insert the old hash and the script will compare them

Author  : Ama
"""
import hmac
import hashlib
import sys


def main():
    print("*" * 50)
    print("Hi, welcome to the HMAC hash calculator!")
    print("Here you can calculate a keyed HASH for a file, using HMAC has function.")
    print("*" * 50)

    print("")
    file_name = input("##Insert name of the file: ")
    key = input("##Insert hash key: ")
    print("")

    print("##Calculating HMAC...")
    try:
        hash = calculate_hash(file_name, key)
    except:
        print("Error! Check file name...")
        sys.exit()
    print("##Hash:")
    print("#" * 20)
    print(hash)
    print("#" * 20)
    print("")

    opt = ""
    while(opt not in ("C", "Q")):
        print("##Please select option: ")
        print("  C: Check calculated file hash against old hash")
        print("  Q: Quit")
        opt = input("##Option: ").upper()
        if (opt not in ("C", "Q")):
            print("")
            print("Wrong selection...")
            print("")

    if opt == "C":
        old_hash = input("##Insert old hash: ")
        print("Checking...")
        is_same = check_hash(old_hash, hash)
        if is_same:
            print("##CORRECT: The two hashes correspond!")
            print("##File was NOT modified")
        else:
            print("##ERROR: The two hashes are different!!")
            print("##File was modified since last check!")

    sys.exit()



def calculate_hash(file_name, key):
    """
    This function calculates hash value using HMAC hash function.
    In order to calculate the file hash, the function takes in input two parameters:
     _file name
     _key : 'key' is the user provided key passed to the HMAC algorithm to calculate hash
    """

    key = hashlib.sha512(key.encode()).digest()
    digest_maker = hmac.new(key, None, hashlib.sha512)

    with open(file_name, "rb") as f:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    digest = digest_maker.hexdigest()

    return digest


def check_hash(old_hash, new_hash):
    """
    Given to input hashes , the function compares them using the hmac.compare_digest function
    Output
      _True  : if the two hashes correspond
      _False : Otherwise
    """
    result = hmac.compare_digest(old_hash, new_hash)

    return result


if __name__=="__main__":
    main()
