from PIL import Image

def decode_message(path: str):

    img = Image.open(path).convert("RGB")
    pixels = img.getdata()

    bits = []
    for r, g, b in pixels:
        bits.extend([r & 1, g & 1, b & 1])

    bytes_data = bytearray()
    for i in range(0, len(bits), 8):
        byte_group = bits[i:i+8]
        if len(byte_group) < 8:
            break
        byte_value = int((''.join(map(str, byte_group))), 2)
        if byte_value == 0:
            break
        bytes_data.append(byte_value)

    return bytes(bytes_data)

if __name__ == "__main__":

    image_path = "K:\\Programs\\PythonPrograms\\Cryptography_Algorithms\\Steganography\\final_image.png"
    bytes_msg = decode_message(path=image_path)

    print(bytes_msg.decode())
