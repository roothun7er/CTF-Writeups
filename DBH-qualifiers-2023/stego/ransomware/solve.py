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