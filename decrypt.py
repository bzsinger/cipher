def decrypt(text):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) - 1)
    return encrypted_text
