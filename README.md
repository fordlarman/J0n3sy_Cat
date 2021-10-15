# J0n3sy_Cat!

![Screen Shot 2021-10-15 at 3 21 01 pm](https://user-images.githubusercontent.com/62928781/137431810-fb17782a-7573-4dde-8aa9-f7449483478d.png)



A Remote Access Trojan (RAT) backdoor executable generator for MacOS. 
*For Educational purposes only

Inpsired by hacking tools such as the Metasploit framework and FatRat, J0n3sy_Cat is a RAT backdoor scripting tool used to generate a .dmg trojan file allowing users to connect to target machines once deployed.

FatRat - https://github.com/Screetsec/TheFatRat

Metasploit - https://www.metasploit.com/

This script generates a phony .dmg package that once installed will launch a hidden tcp connection link. Once the attacker is confident the exploit has been deployed, they can connect to the target allowing them to execute commands remotely an undetected. To hide communications J0n3sy_Cat uses a single symmetric encryption key to ensure all traffic is unreadable, once a backdoor is compromised a new key can be generated for future exploits.

Features:
 - Encrypted communication
 - File Transfer
 - Remote command execution
 - Generate .dmg
 
This project is intended to improve my (Python) programming skills, and knowledge within the field of cyber/info security.
Q: Why J0n3sy_Cat?
A: Networking programs such as 'netcat' and 'Apache Tomcat' inspired me to call it (something) feline related. "Jonesy" is the name of the cat from the film 'Alien'(1979), A favourite of mine.
