import base64


### HELPERS

def hamming_distance(s1, s2):
    """
    Compute hamming distance between two strings.
    Assumes the two strings are the same length.
    """
    b1 = bytearray(s1, encoding='ascii')
    b2 = bytearray(s2, encoding='ascii')

    d = 0
    for i in range(len(b1)):
        diff = b1[i] ^ b2[i]
        num_diff_bits = bin(diff).count("1")
        d += num_diff_bits

    return d


def iterate_file():
    """
    Read in encrypted base64 file and return its contents as bytes.

    Note: Python prints printable hex characters as is, and unprintable hex
    characters with a preceeding \x and two characters.
    """
    # File in base64
    filename = 'files/6.txt'

    # Decode base64 into bytes
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()

        # TODO: answer question: do we do anything with newlines?
        data_bytes = base64.b64decode(data)
        print(data_bytes)
        return data_bytes


### DECRYPT

def decrypt_xor(encrypted_msg):

    ### Find candidate keysize
    for keysize in range(2, 41):

        # Find edit distance between first two keysized blocks
        ## Python slices on byte objects
        block_1 = encrypted_msg[:keysize]
        block_2 = encrypted_msg[keysize:keysize+keysize]

        print('block_1: ', block_1)
        print('block_2: ', block_2)


        # Optional: try different strategies

        # Normalize result (divide by keysize)

    ### Set up ciphertext for decryption

        # Break up ciphertext into keysized blocks

        # Transpose blocks and apply single-character XOR

        # Combine single-character XOR keys


        pass


if __name__ == "__main__":

    s1 = 'this is a test'
    s2 = 'wokka wokka!!!'
    hamming_test = hamming_distance(s1, s2)
    print('Testing hamming distance:')
    print('Expected: 37')
    print('Actual  :', hamming_test)

    print()
    print('Test iterate_file')
    encrypted_msg = iterate_file()

    print()
    print('Test decrypt_xor')
    decrypt_xor(encrypted_msg)

