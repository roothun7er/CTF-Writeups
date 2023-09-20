#DBH #deutschlandsbesterhacker #challanges #cybersecurity 

---
> hun7er Cybersecurity | Sep 18th, 2023
---
<br />

## Instructions


```
Die Musik verschmilzt mit meiner Seele und nimmt mich mit auf eine Reise ins Ungewisse, 
wo mir der Kern des Liedes neue Horizonte eröffnet.

**Hinweis:** Flag entspricht nicht dem klassischen DBH{}-Format

Dateien: ca8f82c65b9cb300ee7aa575dc4c9c9244076208e 756864ae3c971f3b2c3a92d combined.wav
```

* Download the `combined.wav` file
---
<br />

## Install requirements


Install Sonic Visualiser:
```bash 
sudo apt install sonic-visualiser -y
```
---
<br />

## Analyzing

Open the combined.wav file in Sonic Visualizer :
```bash
sonic-visualiser combined.wav 
```

* If you listing to the audio you will hear no anomalies 

* On the first look you will see nothing interesting

<br />


Add an Spectrogram to your Projekt
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918191414.png' alt='Add an Spectrogram'>
* After you change the spectrum and analyze your file you will find anomalies on the Timestamp 2:19 min

<br />

Anomalies:
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918191906.png' alt='Anomalies'>
* if you look closer and zoom in you will see an pattern.

<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918192109.png' alt='Anomalies Zoomed'>
* it looks like Morsecode
---
<br />

## Cyberchef

Open Cyberchef in your browser:
```https
https://cyberchef.org/
```

Setting up Cyberchef:
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918192632.png' alt='Setting up Cyberchef'>
+ Type `morse` in the search field and move `To Morse Code` per drag and drop to the Recipe field on the right side

Solve the challenge:
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918192109.png' alt='Solve the challenge1'>
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918193136.png' alt='Solve the challenge2'>
Legende: short = `.`, long = `-`

* Solve the Challenge by following the sort an long periods in the green Spectrogram and type it in the Cyberchef input field with the `short` and `long` 

+ After you have it right, you solved the challenge Congrats.

---
<br />

## The Flag

Don't forgot the hint from the instructions
```txt
**Hinweis:** Flag entspricht nicht dem klassischen DBH{}-Format
```

The flag:
```txt
DBH{DBH-LIEBE-AUDIOS!}
```
---
