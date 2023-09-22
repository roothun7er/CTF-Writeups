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

* download the file `combined.wav`
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

Open the file `combined.wav` in `Sonic Visualizer` with the following command:
```bash
sonic-visualiser combined.wav 
```

* if you listen to the audio you will not hear any anomalies. 

* at first look you will not see anything interesting

<br />

Add a spectrogram to your project:
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918191414.png' alt='Add an Spectrogram'>
* After changing the spectrum and analyzing your file, you will find anomalies at the timestamp 2:19 min.

<br />

Anomalies:

<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918191906.png' alt='Anomalies'>
* if you look closer and zoom in you can see a pattern.

<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918192109.png' alt='Anomalies Zoomed'>
* it looks like morse code

---
<br />

## Cyberchef

Open Cyberchef in your preferred browser:
```https
https://cyberchef.org/
```

Setting up Cyberchef:
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918192632.png' alt='Setting up Cyberchef'>
* type `morse` in the search box and drag and drop `To Morse Code` into the `Recipe` box on the right.

Solve the challenge:
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918192109.png' alt='Solve the challenge1'>
<img src='https://github.com/hun7erCybersecurity/CTF-Writeups/blob/main/DBH-qualifiers-2023/stego/audio/img/Pasted image 20230918193136.png' alt='Solve the challenge2'>
Legend: short = `.`, long = `-`

* solve the challenge by following the short and long time periods in the green `spectrogram` and entering them in the `cyberchef` input field with `short` and `long` 

* if you did it right, you solved the challenge Congratulations.

---
<br />

## The Flag

Don't forget the hint in the instructions:
```txt
**Hinweis:** Flag entspricht nicht dem klassischen DBH{}-Format
```

The flag:
```txt
DBH{DBH-LIEBE-AUDIOS!}
```
---
