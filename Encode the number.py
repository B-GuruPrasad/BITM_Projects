def encode_number(n):
    str_n=str(n)
    encode_str=""
    for digit in str_n:
        squared_digit=int(digit)**2
        encode_str+=str(squared_digit)
    encoded_value=int(encoded_str)
    return encoded_value
n=int(input())
result=encode_number(n)
print(result)