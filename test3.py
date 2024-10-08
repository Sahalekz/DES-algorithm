import random
import math

def format_plaintext():
    plain_text = input("Enter the plain text")
    plain_text_lst = []
    padding_required=len(plain_text)%8
    if padding_required !=0:
        plain_text=plain_text.ljust(8*math.ceil(len(plain_text)/8),'0')
    print(plain_text)
    for i in plain_text:
        plain_text_lst.append(i)
    print(plain_text_lst)
    return plain_text_lst


def conv_to_binary():
    plain_text_lst=format_plaintext()
    split_64_binary = []
    for j in range(8):
        temp = plain_text_lst.pop(0)
        ASCII = ord(temp)
        Binary = bin(ASCII)[2:].zfill(8)
        for k in Binary:
            split_64_binary.append(k)
    return split_64_binary


def gen_permutation_table():
    permutation_table = []
    for i in range(1, 65):
        permutation_table.append(i)
    random.shuffle(permutation_table)
    return permutation_table


def mapping():
    permuted_table = []
    p_table = gen_permutation_table()
    binary_table = conv_to_binary()
    for i in p_table:
        permuted_table.append(binary_table[int(i) - 1])
    print(f"Split 64 binary {binary_table}")
    print(f"permuted table {permuted_table}")


mapping()
