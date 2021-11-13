alphabets = 'abcdefghijklmnopqrstuvwxyz '
braille = ['100000', '110000', '100100', '100110', '100010',
           '110100', '110110', '110010', '010100', '010110',
           '101000', '111000', '101100', '101110', '101010',
           '111100', '111110', '111010', '011100', '011110',
           '101001', '111001', '010111', '101101', '101111',
           '101011', '000000']
a_to_b = {a:b for a,b in zip(alphabets,braille)}

def solution(s):
    return_str = ''
    for alphabet in s:
        if alphabet.isupper():
            return_str += '000001'
        return_str += a_to_b[alphabet.lower()]
    
    return return_str