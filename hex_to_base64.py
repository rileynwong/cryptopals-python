from base64 import b64encode, b64decode


def hex_to_base64(hex):
    # convert hex string to base64
    print('hex to base64')
    b64 = b64encode(bytes.fromhex(hex)).decode()

    return b64


if __name__ == "__main__":

    s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64 = hex_to_base64(s)

    print('Expected, Actual')
    print('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
    print(b64)
