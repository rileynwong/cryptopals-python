import numpy


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

    print('Expected, Actual')
    print('746865206b696420646f6e277420706c6179')

    print(xor_result)
