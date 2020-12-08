# J0n3sy_Cat
A Remote Access Trojan (RAT) backdoor executable generator and server project. 
*For Educational purposes only

Inpsired by hacking tools such as the Metasploit framework and FatRat, J0n3sy_Cat is a RAT backdoor tool used to generate an executable target file and connect to that target file once activated.

Using python modules the application can connect to a target and communicate via a subprocess allowing the attacker to execute commands remotely an undetected. To hide communications J0n3sy_Cat uses a single symmetric encryption key, once a backdoor is compromised a new key can be generated for future exploits.

Features:
 - Encrypted communication
 - Screenshot target machine
 - Remote command execution
 - Generate executable
 
This project is intended to improve my (Python) programming skills, and knowledge within the field of cyber/info security.
Q: Why J0n3sy_Cat?
A: Networking programs such as 'netcat' and 'Apache Tomcat' inspired me to call it (something) cat. "Jonesy" is the name of the cat from the film 'Alien'(1979), A favourite of mine.
