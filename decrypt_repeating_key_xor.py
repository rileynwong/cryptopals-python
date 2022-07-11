import base64, math


### HELPERS

def hamming_distance(b1, b2):
    """
    Compute hamming distance between two bytestrings.
    Assumes the two bytestrings are the same length.
    """
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
    characters with a preceeding \\x and two characters.
    """

    # File in base64
    filename = 'files/6.txt'

    # Decode base64 into bytes
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()

        # TODO: answer question: do we do anything with newlines?
        data_bytes = base64.b64decode(data)
        # print(data_bytes)
        return data_bytes


### DECRYPT

def find_candidate_keysize(encrypted_msg):

    minimum_hamming_distance = math.inf
    keysize_candidate_min = 0

    ### Find candidate keysize
    for keysize in range(2, 41):

        # Find edit distance between first two keysized blocks
        ## Python slices on byte objects
        block_1 = encrypted_msg[:keysize]
        block_2 = encrypted_msg[keysize:keysize+keysize]

        print('block_1: ', block_1)
        print('block_2: ', block_2)

        keysize_hamming_distance = hamming_distance(block_1, block_2)

        # Normalize result (divide by keysize)
        normalized_distance = keysize_hamming_distance / keysize
        print(normalized_distance)

        if normalized_distance < minimum_hamming_distance:
            minimum_hamming_distance = normalized_distance
            keysize_candidate_min = keysize

    ## Possible additional strategies to try:

    # Strategy: Find 2-3 minimum edit distances and corresponding keysizes
        # Create a dictionary{keysize, edit_distance} and query min 3.

    # Strategy: Take two pairs of blocks and average the distances.

    print('Minimum hamming distance found: ', minimum_hamming_distance)
    print('Corresponding keysize candidate: ', keysize_candidate_min)

    return keysize_candidate_min


def decrypt_xor(keysize):
    print('Trying keysize: ', keysize)

    ### Set up ciphertext for decryption

        # Break up ciphertext into keysized blocks

        # Transpose blocks and apply single-character XOR

        # Combine single-character XOR keys



if __name__ == "__main__":

    s1 = 'this is a test'
    s2 = 'wokka wokka!!!'
    b1 = bytearray(s1, encoding='ascii')
    b2 = bytearray(s2, encoding='ascii')

    hamming_test = hamming_distance(b1, b2)
    print('Testing hamming distance:')
    print('Expected: 37')
    print('Actual  :', hamming_test)

    encrypted_msg = iterate_file()

    print()
    print('Test find_candidate_keysize')
    keysize = find_candidate_keysize(encrypted_msg)

    print()
    print('Test decrypt_xor')
    decrypt_xor(keysize)
