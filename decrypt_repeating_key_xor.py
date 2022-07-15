import base64, math

from single_byte_xor import find_single_char_xor_candidate, byte_xor


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


def read_base64_file_as_bytes():
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


def transpose(l):
    """ Given a list of lists, return the transposition. """
    transposed = list(map(list, zip(*l)))
    return transposed


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

        # print('block_1: ', block_1)
        # print('block_2: ', block_2)

        keysize_hamming_distance = hamming_distance(block_1, block_2)

        # Normalize result (divide by keysize)
        normalized_distance = keysize_hamming_distance / keysize
        # print(normalized_distance)

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


def find_candidate_key(encrypted_msg, keysize):
    print('Trying keysize: ', keysize)
    blocks = []

    # Break up ciphertext into keysized blocks
    blocks = [list(encrypted_msg[i:i + keysize]) for i in range(0, len(encrypted_msg), keysize)]

    print('Blocks length: ', len(blocks))
    print('Blocks[5] length: ', len(blocks[5]))

    # print(blocks)
    # TODO: don't use this one HACK cryptographers hate!
    # Drop blocks < keysize length
    uniform_blocks = [block for block in blocks if len(block) == keysize]

    # Transpose blocks and apply single-character XOR
    transposed = transpose(uniform_blocks)
    print('Transposed length: ', len(transposed))

    key = ''
    for transposed_block in transposed:
        result = find_single_char_xor_candidate(transposed_block)
        print('Result for block: ')
        print(result)
        print()
        candidate, score_min, best_result = result

        key += chr(candidate)


    # Combine single-character XOR keys
    print('Key:')
    bytearray_key = bytearray(key, encoding='ascii')
    print(bytearray_key)

    return bytearray_key


def decrypt_xor(encrypted_msg, key):
    """
    Given an encrypted message and key, use xor and return decrypted message.

    Break up encrypted message into key-sized blocks, apply XOR, append the
    decrypted result.
    """

    decrypted_msg = bytearray()

    keysize = len(key)
    blocks = [encrypted_msg[i:i + keysize] for i in range(0, len(encrypted_msg), keysize)]

    for encrypted_block in blocks:
        # Apply xor on the key and block
        print('encrypted_block: ', encrypted_block)
        xor_result = byte_xor(encrypted_block, key)

        decrypted_msg += xor_result


    return decrypted_msg


if __name__ == "__main__":

    s1 = 'this is a test'
    s2 = 'wokka wokka!!!'
    b1 = bytearray(s1, encoding='ascii')
    b2 = bytearray(s2, encoding='ascii')

    hamming_test = hamming_distance(b1, b2)
    print('Testing hamming distance:')
    print('Expected: 37')
    print('Actual  :', hamming_test)

    encrypted_msg = read_base64_file_as_bytes()

    print()
    print('Test find_candidate_keysize')
    keysize = find_candidate_keysize(encrypted_msg)

    print()
    print('Test find_candidate_key')
    key = find_candidate_key(encrypted_msg, keysize)
    print('Key: ', key)

    # Use key to decrypt input
    print()
    print('Test decrypt_xor')
    decrypted_msg = decrypt_xor(encrypted_msg, key)
    print(decrypted_msg)


