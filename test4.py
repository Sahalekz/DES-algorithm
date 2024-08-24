import math

plain_text = input("Enter the plain text")
plain_text_lst = []
padding_required=len(plain_text)%8
final_plaintext_size=8*int(math.ceil(len(plain_text))/8)
if padding_required !=0:
    plain_text=plain_text.ljust(final_plaintext_size,'0')
print(plain_text)
for i in plain_text:
    plain_text_lst.append(i)
