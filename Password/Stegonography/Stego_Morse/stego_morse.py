from cv2 import cv2
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce

img = np.array(cv2.imread('../cat_1.jpg'))


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def morse(message):
    cipher = ''
    cipher_array = []
    for letter in message.upper():
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    for char in cipher:
        if char == '.':
            cipher_array.append('0000')
        elif char == '-':
            cipher_array.append('1111')
        else:
            cipher_array.append('0101')
    return cipher_array

def encode(img,pixels_h,pixels_v,message):
    img = img.reshape(3,pixels_h*pixels_v)
    message = morse(message)
    img[0][0] = len(message)
    for i in range(1,len(message)+1):
        bits = format(img[0][i],'08b')
        bits = bits[:4] + message[i-1]
        img[0][i] = int(bits,2)
    img =  img.reshape(pixels_h,pixels_v,3)
    return img

def decode(img,pixels_h,pixels_v):
    img = img.reshape(3,pixels_h*pixels_v)
    message_len = img[0][0]
    message_arr = []
    for i in range(message_len):
        bits = format(img[0][i],'08b')[-4:]
        if bits == '0000':
            message_arr.append('.')
        elif bits == '1111':
            message_arr.append('-')
        elif bits == '0101':
            message_arr.append(' ')
    message = reduce(lambda a, b : a+str(b), message_arr)
    message = anti_morse(message)
    return message

def anti_morse(message):
    message += ' '
    decipher = ''
    citext = ''
    i=1
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
 
    return decipher



new_img = encode(img,img.shape[0],img.shape[1],"Hail Hitler")
print(decode(new_img,new_img.shape[0],new_img.shape[1]))


cv2.imshow("Cat", new_img)
cv2.waitKey(0)