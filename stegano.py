import numpy as np
import cv2
import os

def read_usb_file(str_filepath: str) -> str:
    with open(str_filepath, 'r') as file:
        str_message = file.read()
    return str_message

def embed_message_into_image(img_filepath: str, str_message: str) -> np.array:
    img = cv2.imread(img_filepath)
    if img is None:
        print("Image not found. Check the file path.")
        return None

    arr_message = [format(ord(i), '08b') for i in str_message]
    lst_data = []
    for element in arr_message:
        lst_data.extend(element)

    int_point = 0
    for int_values in img:
        for pixel in int_values:
            int_r, int_g, int_b = map(int, pixel)
            if int_point < len(lst_data):
                pixel[0] = int(bin(int_r)[:8 - 1] + lst_data[int_point], 2)
                int_point += 1
            if int_point < len(lst_data):
                pixel[1] = int(bin(int_g)[:8 - 1] + lst_data[int_point], 2)
                int_point += 1
            if int_point < len(lst_data):
                pixel[2] = int(bin(int_b)[:8 - 1] + lst_data[int_point], 2)
                int_point += 1
            if int_point >= len(lst_data):
                break
    return img

def save_embedded_image(img: np.array, new_img_filepath: str) -> None:
    cv2.imwrite(new_img_filepath, img)

def main_steganography() -> None:
    str_filepath = "/Users/ujin/steganography/SPAI.txt"
    img_filepath = "/Users/ujin/steganography/tiger.jpg"
    new_img_filepath = "/Users/ujin/steganography/new_image.png"
    
    str_message = read_usb_file(str_filepath)
    embedded_img = embed_message_into_image(img_filepath, str_message)
    
    if embedded_img is not None:
        save_embedded_image(embedded_img, new_img_filepath)
        print("Steganography process completed.")

if __name__ == '__main__':
    main_steganography()
