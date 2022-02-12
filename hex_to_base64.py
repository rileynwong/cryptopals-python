from base64 import b64encode, b64decode
import numpy


def hex_to_base64(hex):
    # convert hex string to base64
    print('hex to base64')
    b64 = b64encode(bytes.fromhex(hex)).decode()

    return b64


def xor(hex_buffer_1, hex_buffer_2):

    # hex to bytestrings
    bytes_buffer_1 = bytes.fromhex(hex_buffer_1)
    bytes_buffer_2 = bytes.fromhex(hex_buffer_2)

    b1 = numpy.frombuffer(bytes_buffer_1, dtype='uint8')
    b2 = numpy.frombuffer(bytes_buffer_2, dtype='uint8')

    # xor bytestrings
    xor_bytes = (b1 ^ b2)

    # convert back to hex
    xor_hex = xor_bytes.tobytes().hex()

    return xor_hex


if __name__ == "__main__":

    buffer_1 = '1c0111001f010100061a024b53535009181c'
    buffer_2 = '686974207468652062756c6c277320657965'
    xor_result = xor(buffer_1, buffer_2)

    print(xor_result)

""" set 1
    s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64 = hex_to_base64(s)
    print(b64)
"""
