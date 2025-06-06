from PIL import Image


def image_to_bytes(path: str):
    image = Image.open(path).convert("RGB")
    pixels = image.getdata()

    byte_data = bytearray()
    for r, g, b in pixels:
        byte_data.extend([r, g, b])

    return byte_data


def embed_message_bytes(message: bytes, path: str):

    bytes_data = image_to_bytes(path=path)

    message_bits = []
    for byte in message:
        bits = bin(byte)[2:].rjust(8, '0')
        message_bits.extend([int(b) for b in bits])

    bit_pos = 0
    bitmask = 1 << bit_pos

    modified_bytes = bytearray()
    for i, byte in enumerate(bytes_data):
        modified_byte = ((byte & ~bitmask) | (message_bits[i]) if i < len(message_bits) else byte)
        modified_bytes.append(modified_byte)
    
    return modified_bytes


def create_image(message: bytes, path: str, width: int, height: int):

    bytes_data = embed_message_bytes(message=message, path=path)

    pixels = [
        tuple(bytes_data[j:j+3]) for j in range(0, len(bytes_data), 3)
    ]

    img = Image.new("RGB", (width, height))
    img.putdata(pixels)
    img.save("final_image.png")

    return None


def read_file_data(path: str):

    with open(path, 'r') as file:
        content = file.read()
    
    return content + "\0"


if __name__ == "__main__":

    file_path = "achievement_list.txt"
    image_path = "picture.png"
    
    secret_msg = read_file_data(path=file_path)
    create_image(message=secret_msg.encode(), path=image_path, width=1024, height=1024)
