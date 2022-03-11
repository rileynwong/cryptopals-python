from itertools import repeat

from single_byte_xor import byte_xor


    # ascii_byte_repeated = bytearray(repeat(decimal, len(message)))
    # xor_result = byte_xor(message, ascii_byte_repeated)

def repeating_key_xor(message, key):

    # + 1 so the repeating key can be truncated to message length
    repeat_n = (len(message) / len(key)) + 1
    repeating_key = ''.join(repeat(key, int(repeat_n)))

    byte_msg = bytearray(message, encoding='ascii')
    byte_key = bytearray(repeating_key, encoding='ascii')

    xor_result = byte_xor(byte_msg, byte_key)
    return xor_result


if __name__ == "__main__":

    message = ("Burning 'em, if you ain't quick and nimble\n"
    "I go crazy when I hear a cymbal")
    key = 'ICE'

    expected = ("0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272"
    "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f")

    xor_result = repeating_key_xor(message, key)
    actual = xor_result.hex()

    print('expected: ', expected)
    print('actual:   ', actual)
