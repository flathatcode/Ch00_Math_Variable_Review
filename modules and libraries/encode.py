

def encode(key, string):
    '''
    Encode a message using encryption key
    :param key: encryption key
    :param string: message to encrypt
    :return: encrypted message
    '''
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return encoded_string