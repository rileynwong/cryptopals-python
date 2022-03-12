from itertools import repeat
from collections import defaultdict
from math import inf
from string import printable


"""
Frequency table source: http://millikeys.sourceforge.net/freqanalysis.html
"""
ASCII_FREQUENCIES = {
  ' ': 18.74,
  'E': 9.60,
  'T': 7.02,
  'A': 6.21,
  'O': 5.84,
  'I': 5.22,
  'N': 5.21,
  'H': 4.87,
  'S': 4.77,
  'R': 4.43,
  'D': 3.52,
  'L': 3.20,
  'U': 2.25,
  'M': 1.94,
  'C': 1.88,
  'W': 1.82,
  'G': 1.66,
  'F': 1.62,
  'Y': 1.56,
  'P': 1.31,
  ',': 1.24,
  '.': 1.21,
  'B': 1.19,
  'K': 0.74,
  'V': 0.71,
  '"': 0.67,
  '\'': 0.44,
  '-': 0.26,
  '?': 0.12,
  'X': 0.12,
  'J': 0.12,
  ';': 0.08,
  '!': 0.08,
  'Q': 0.07,
  'Z': 0.07,
  ':': 0.03,
  '1': 0.02,
  '—': 0.01,
  '0': 0.01,
  ')': 0.01,
  '*': 0.01,
  '(': 0.01,
  '2': 0.01,
  '’': 0.01,
  '`': 0.01,
  '“': 0.01,
  '”': 0.01,
  '3': 0.01,
  '9': 0.01,
  '5': 0.01,
  '4': 0.01,
}


# Takes two frequency dictionaries and computes a similarity score using the
# sum of squared differences.
def sum_of_squared_residuals(f1, f2):
    ks = f1.keys() | f2.keys()
    residuals = [(f1[k] - f2[k]) ** 2 for k in ks]
    return sum(residuals)


def byte_xor(ba1, ba2):
    """
    XOR two byte strings.
    Truncates to the shorter length.
    """
    return bytes([a ^ b for a, b in zip(ba1, ba2)])


def character_frequencies(input):
    input = input.lower()

    # Calculate character counts
    counts = defaultdict(lambda: 0.0)
    for c in input:
        counts[chr(c)] += 1

    # Calculate character frequencies
    input_len = len(input)
    freqs = defaultdict(lambda: 0.0)
    for k, v in counts.items():
        freqs[k] = (v / input_len) * 100

    return freqs


def iterate_ascii(hex_input):
    buffer = bytes.fromhex(hex_input)

    best_result = None
    best_dec = None
    score_min = inf
    # Iterate through decimal set of possible ASCII
    for decimal in range(0, 127):
         # print('trying dec: ', str(decimal))

        # Convert decimal to formatted hex
        ascii_byte_repeated = bytearray(repeat(decimal, len(buffer)))

        # Try hex value as single_hex key
        xor_result = byte_xor(buffer, ascii_byte_repeated)
        # print('xor_result: ', xor_result)

        score = sum_of_squared_residuals(defaultdict(lambda: 0.0, ASCII_FREQUENCIES), character_frequencies(xor_result))
        # print('score: ', score)
        if score < score_min:
            score_min = score
            best_result = xor_result
            best_dec = decimal

    return (best_dec, score_min, best_result)


def iterate_file():
    filename = 'files/4.txt'

    with open(filename, 'r', encoding='utf-8') as f:
        iterated = [iterate_ascii(line) for line in f]
        iterated.sort(key=lambda tuple: tuple[1])

        for result in iterated:
            bytes = result[2]
            try:
                bs = set(bytes.decode('ascii'))
                if bs.issubset(printable):
                        print(result)

            except:
                pass


if __name__ == "__main__":

    iterate_file()

    buffer = '7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f'
    # buffer = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    # print(iterate_ascii(buffer))

