alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encrypt_or_decrypt):

    if encrypt_or_decrypt == "decode":
        shift_amount *= -1

    encrypted_or_decrypted_msg = ""
    for letter in original_text:
        new_index = alphabet.index(letter) + shift_amount
        new_index %= 26
        new_letter = alphabet[new_index]
        encrypted_or_decrypted_msg += new_letter
    print(f"Here is the {encrypt_or_decrypt}d result: {encrypted_or_decrypted_msg} ")


caesar(original_text=text, shift_amount=shift, encrypt_or_decrypt=direction)

