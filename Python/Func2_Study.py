def generate_enc_key():
    enc_key = {'a': 'p', 'b': 'y', 'c': 'w', 'd': 'f', 'e': 'n', 'f': 'd', 'g': 'k', 'h': 's', 'i': 'r', 'j': 'z', 'k': 'g', 'l': 'v', 'm': 'q', 'n': 'e', 'o': 'u', 'p': 'a', 'q': 'm', 'r': 'i', 's': 'h', 't': 'x', 'u': 'o', 'v': 'l', 'w': 'c', 'x': 't', 'y': 'b', 'z': 'j', ' ': ' ', '': ''}
    return enc_key

def convert_key():
    dec_key = {'p': 'a', 'y': 'b', 'w': 'c', 'f': 'd', 'n': 'e', 'd': 'f', 'k': 'g', 's': 'h', 'r': 'i', 'z': 'j', 'g': 'k', 'v': 'l', 'q': 'm', 'e': 'n', 'u': 'o', 'a': 'p', 'm': 'q', 'i': 'r', 'h': 's', 'x': 't', 'o': 'u', 'l': 'v', 'c': 'w', 't': 'x', 'b': 'y', 'j': 'z', ' ': ' ', '': ''}
    return dec_key

def enc_dec_text(any_text, enc_dec_key):
    new_text = ''
    for letter in any_text:
        letter = enc_dec_key[letter]
        new_text += letter
    return new_text


def test_all():
    text = 'hello world'
    enc_key = generate_enc_key()
    encrypted_text = enc_dec_text(text, enc_key)

    dec_key = convert_key()
    decrypted_text = enc_dec_text(encrypted_text, dec_key)

    print('Original text: ', text)
    print(encrypted_text)
    print('Restored text: ', decrypted_text)


test_all()



