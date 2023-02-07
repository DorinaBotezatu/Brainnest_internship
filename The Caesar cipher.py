"""
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar.
It encrypts letters by shifting them over by a certain number of places in the alphabet. We call the length of shift the key.
For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift the encrypted letters in the opposite direction.
 This program lets the user encrypt and decrypt messages according to this algorithm.

When you run the program, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
"""

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]


def encrypt_message():
    message_final = []
    key_input = int(input("Please enter the key (0 to 26) to use."))
    message_to_encrypt = input("Enter the message to encrypt.")
    for character in message_to_encrypt:
        if character.upper() not in alphabet:
            message_final.append(character)
        else:
            index = alphabet.index(character.upper())
            if key_input + index > len(alphabet) - 1:
                index = key_input - (len(alphabet) - index)
                message_final.append(alphabet[index])
            else:
                message_final.append(alphabet[index + key_input])

    return "".join(message_final)


def decrypt_message():
    message_final = []
    key_input = int(input("Please enter the key (0 to 26) to use."))
    message_to_decrypt = input("Enter the message to decrypt.")
    for character in message_to_decrypt:
        if character.upper() not in alphabet:
            message_final.append(character)
        else:
            index = alphabet.index(character.upper())
            if index - key_input < 0:
                index = (len(alphabet) - abs(index - key_input))
                message_final.append(alphabet[index])
            else:
                message_final.append(alphabet[index - key_input])

    return "".join(message_final).capitalize()


def Caesar_cipher():
    e_d_answer = input("Do you want to (e)ncrypt or (d)ecrypt?")
    if e_d_answer == "e":
        encrypted_message = encrypt_message()
        print(encrypted_message)
    if e_d_answer == "d":
        decrypted_message = decrypt_message()
        print(decrypted_message)


if __name__ == "__main__":
    Caesar_cipher()
