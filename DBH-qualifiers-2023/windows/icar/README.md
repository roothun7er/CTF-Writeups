#DBH #deutschlandsbesterhacker #challanges #cybersecurity 

---
> roothun7er | Sep 23th, 2023
---
<br />

## Instructions


```
iCar ist ein experimentelles Anti-Virus Produkt der Firma DBHLabs.
Diese Beta-Version kann Testviren erkennen und versucht, diese zu analysieren. 
Damit die Beta-Version nicht "die Runde macht", wird geprüft, 
ob die Beta-Version auf einem Computer der DBHLabs läuft. 
Die Beta-Version kann von anderen Anti-Virus-Lösungen als Virus eingestuft werden, 
ist jedoch absolut ungefährlich.

Dateien: iCar.exe
SHA256 checksum: 52b6ab638a80326ef64504506fa51f868a149bff1bc01a0b4fdfd7039caa281b
```


---
<br />

## Setup Windows 10/11 requirements


Since `iCar.exe` is not a malicious file, but it is detected as such by Windows Defender, 
we need to work around this by changing a few things:

* first of all start a Windows 10/11 virtual machine in your preffered virtualization tool.

* open `powershell` as `administrator`

* we must add some exception rules to Windows Defender

<br />

Add `icar.exe` and `eicar.txt` as an exception rule to Windows Defender with the following commands:
```powershell
Add-MpPreference -ExclusionPath "$env:USERPROFILE\Downloads\iCar.exe"
Add-MpPreference -ExclusionPath "$env:USERPROFILE\Downloads\eicar.txt"
```
* nice, now we have set the exception path to the specific files


<br />

Check if the exception rules have been executed correctly with the following command:
```powershell
Get-MpPreference | Select-Object -ExpandProperty ExclusionPath
```
* if everything is correct we have set up the Windows environment to perform the last step in this section for now.

* now we can download the file `iCar.exe` to the built-in `Downloads` folder without a Windows defender winning

---
<br />

## Analysis of the program behavior

<br />

Navigate to your `Download` folder using the following command:
```powershell
cd $env:USERPROFILE\Downloads
```
<br />

Open the `icar.exe` file in `powershell` with the following command:
```powershell
.\icar.exe
```

<br />

After starting `iCar.exe` you will see the following:
<img src='https://github.com/roothun7er/CTF-Writeups/blob/main/DBH-qualifiers-2023/windows/icar/img/iCar_Start.png' alt='iCar_Start'>

* after launching the `iCar.exe` program we see in the text that the test virus `eicar.txt` must be located in the same directory.

* oh didn't we forget something? 

* we have the wrong `hostname` if you remember the instructions the computer must have an internal name that includes `DBHLabs`.

* let's do this first
<br />


Set a computer name that includes `DBHLabs` and restart the computer with the following command:
```powersell
Rename-Computer -NewName "DBHLabs-1337" -Restart
```
* after the execution of the command the computer will be restarted automatically
---
<br />

## Test Virus Eicar

* after the computer is restarted we need to take care of the test virus mentioned above

* a simple `duckduckgo` search with `icar vi` is enough for the autocomplete to suggest `eicar virus` 

* let's look what we have

<br />

Open the following Hompage in your preffered browser:
```https
https://www.eicar.org/download-anti-malware-testfile/
```
* nice let's try it out it sounds right and plausible

* we have to create a file `eicar.txt`

<br />

Add a file `eicar.txt` containing the payload of the previous web page into the folder `downloads` with the following command:
```powershell
New-Item -ItemType File -Path "$env:USERPROFILE\Downloads\eicar.txt" -Value "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
```
---
<br />

## Solve the challenge

* open `powershell` as `administrator`

Navigate to your `Downloads` folder with the following command:
```powershell
cd $env:USERPROFILE\Downloads
```
* after we have opened the Powershell we check if both files are present in the folder

* if both files are there we can start the program `iCar.exe`

<br />

Open the file `icar.exe` in powershell with the following command:
```powershell
.\icar.exe
```

After the programstart you should see an text like in the following picture:
<img src='https://github.com/roothun7er/CTF-Writeups/blob/main/DBH-qualifiers-2023/windows/icar/img/iCar_solve.png' alt='iCar_solve'>


* if you did it right, you solved the challenge Congratulations.

<br />


Copy the flag and `echo` it in a file `flag.txt` with the following command:
```bash
echo "DBH{e1c4r_t3sTf1l3_i5t_l3g3nDe}" > flag.txt
```
---
<br />

## Watch the flag

<br />

Shows the content of the file `flag.txt` with the following command:
```bash
cat flag.txt
```
Output:
```txt
DBH{e1c4r_t3sTf1l3_i5t_l3g3nDe}
```
---

