from PIL import Image


def encrypt_terrorists_message(image_path: str) -> str:
    """
    This function gets a path to an image and decrypts the hidden message.
    The hidden message is in a format of black pixels, where each pixel's index represents a letter of the message we want
    to encrypt.
    :param image_path: the path of the image that we would like to decrypt
    :return: the decrypted message
    """
    image = Image.open(image_path)
    width, height = image.size
    black_pixel = [j for i in range(width) for j in range(height) if image.getpixel((i, j)) == 1]
    return ''.join([chr(pixel) for pixel in black_pixel])


if __name__ == '__main__':
    print(encrypt_terrorists_message("code.png"))
