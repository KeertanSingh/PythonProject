import base64

def encoder(string):
    encoded = base64.b64encode(string)
    print(f"""******************************
{encoded.decode("utf-8")}
******************************""")


def decoder(string):
    decoded = base64.b64decode(string)
    print(f"""******************************
{decoded.decode("utf-8")}
******************************""")


if __name__ == '__main__':
    print("Welcome to base64 converter")
    data_string = input("Enter the string: ")
    data_byte = bytes(data_string, 'utf-8')
    choose = input("""What do you want:
1. encode
2. decode
>> """)
    if choose == "encode":
        encoder(data_byte)
    elif choose == "decode":
        decoder(data_byte)
    else:
        print("Invalid input.")
