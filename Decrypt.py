def decrypt(text, shift):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) - shift)
    return encrypted_text
