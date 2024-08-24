# DES-algorithm
This code implements a modified version of the Data Encryption Standard (DES) algorithm. DES is a symmetric key algorithm used for encryption and decryption of data. The provided code allows you to encrypt and decrypt a given plaintext using a user-specified key. Below is an explanation of the code components:
1. Key Generation (key_generation()):
Purpose: Generates 16 subkeys from the main key, which are used in the encryption and decryption rounds.
Steps:
It starts by reading the key from the user.
The key is then passed through a Permuted Choice 1 (PC1) to rearrange its bits.
The key is split into two halves and circular left shifts are applied.
A new subkey is generated for each of the 16 rounds using Permuted Choice 2 (PC2).
2. Encryption (encryption()):
Purpose: Encrypts a given plaintext using the generated subkeys.
Steps:
Reads the plaintext and converts it to binary.
Applies an initial permutation (IP) to the binary plaintext.
Splits the permuted plaintext into two halves (Li and Ri).
For each of the 16 rounds:
Expands Ri using an expansion table to match the key length.
XORs the expanded Ri with the subkey for that round.
Applies S-box substitution to reduce the size of the result.
Permutes the result using a permutation table.
XORs the permuted result with Li, and then swaps Li and Ri.
After 16 rounds, combines Li and Ri, applies an inverse initial permutation, and outputs the ciphertext.
3. Decryption (decryption()):
Purpose: Decrypts the ciphertext using the same keys, but in reverse order.
Steps:
Reads the ciphertext and converts it to binary.
Applies the initial permutation (IP).
Similar to encryption, it splits the result into two halves (Li and Ri).
For each of the 16 rounds (in reverse order):
Performs the same operations as in encryption but uses the keys in reverse order.
Combines Li and Ri, applies the inverse initial permutation, and outputs the decrypted plaintext.
4. Helper Functions:
read_plain_text(): Takes the plaintext from the user and pads it to make its length a multiple of 8.
conv_to_binary(): Converts a list of characters into their binary representation.
inv_conv_to_binary(): Converts a list of binary bits back into characters.
mapping(): Rearranges the bits in a binary table according to a specified permutation table.
inverse_mapping(): Reverses the bit permutation process.
read_key(): Reads an 8-character key from the user.
permuted_choice_1(): Applies the PC1 table to the key.
circular_left_shift(): Performs circular left shifts on the key halves.
permuted_choice_2(): Applies the PC2 table to generate a subkey.
split_bits(): Splits a list into two equal halves.
expansion_table(): Expands a 32-bit block into 48 bits.
substitution_box(): Applies S-box substitution to the XOR result.
inv_initial_permutation(): Reverses the initial permutation after encryption or decryption.
5. Permutation and S-box Tables:
initial_permutation_ptable: Initial permutation table for rearranging plaintext bits.
permutation_box_ptable: Permutation table for permuting S-box output.
permuted_choice_1_ptable: Permuted choice 1 table for key generation.
permuted_choice_2_ptable: Permuted choice 2 table for subkey generation.
expansion_box_ptable: Expansion table to expand a 32-bit block to 48 bits.
s_boxes_list: List of S-boxes used in substitution during encryption and decryption.
Execution:
The program prompts the user for a plaintext and a key.
It then performs encryption and displays the ciphertext.
After encryption, it decrypts the ciphertext and outputs the original plaintext to verify correctness.
