import numpy


def single_xor(hex_buffer_1, single_hex):

    # hex to bytestrings
    bytes_buffer_1 = bytes.fromhex(hex_buffer_1)
    bytes_buffer_2 = bytes.fromhex(single_hex)

    b1 = numpy.frombuffer(bytes_buffer_1, dtype='uint8')
    b2 = numpy.frombuffer(bytes_buffer_2, dtype='uint8')

    # xor bytestrings
    xor_bytes = (b1 ^ b2)
    print('xor_bytes: ')
    print(xor_bytes)

    # convert back to hex
    xor_hex = xor_bytes.tobytes().hex()

    return xor_hex



def iterate_hex():
    buffer_1 = '1c0111001f010100061a024b53535009181c'

    # Iterate through decimal set of possible ASCII
    for decimal in range(0, 128):
        print('trying dec: ', str(decimal))

        # Convert decimal to formatted hex
        hex_val = hex(decimal)[2:].zfill(2)

        print('hex_val: ', hex_val)

        # Try hex value as single_hex key
        xor_hex_result = single_xor(buffer_1, hex_val)
        print('xor_hex_result: ', xor_hex_result)

        # Convert hex to ASCII
        bytes_object = bytes.fromhex(xor_hex_result)
        ascii_result = bytes_object.decode("ASCII")

        print('ascii result: ', ascii_result)
        print()


if __name__ == "__main__":

    iterate_hex()
