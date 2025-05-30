# PENETRATION-TESTING-TOOLKIT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: GAIKWAD SANITA SANJAY

*INTERN ID*: CT04DL698

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DISCRIPTION*: 

Part 1: Brute Forcer and Custom Login Server

For the first part of my Pen Testing Toolkit, I created a simulated environment to demonstrate how brute-force attacks work on a login page. I built a simple login server using Python’s Flask framework also protecting it from hackers using a watchdog which gives warning when changes occurs. This server listens on a route '/login' and only accepts POST requests. The server checks if the username and password match predefined values specifically, the username "sanita" and the password "password123". If they match, the server returns Login successful message, otherwise, it responds with Login unsuccessful including a 401 Unauthorized error.

To attack my own made login server I created a Python-based brute-forcer script. This script takes a list of passwords from a text file and automatically attempts to log in using each one, alongside the correct username. As soon as the script receives a successful response from the server, it stops and prints out the cracked password. This helped me understand how attackers might exploit weak credentials and how important it is for web applications to implement rate limiting, lockout mechanisms, or CAPTCHA.

Getting everything to run correctly required trial and error. I ran these codes on multiple platforms like Trea, VS Code, and IDLE. Each one gave me a slightly different experience with debugging, file path formatting, and virtual environments. For example, Trea was helpful when I needed to run multiple files at a time on same terminal, while VS Code’s structure helped to solve errors more efficiently.

I also faced some real-world debugging challenges. The server sometimes wouldn’t load in the browser due to incorrect port usage or because I was trying to access a POST endpoint via a browser (which doesn’t work unless you use Postman or script it). Also the issue occurred when the login server wasn't active and to keep both code running at a time was a huge task to fix but eventually I figured out and fixed the issue, which deepened my understanding of local Flask servers and how 127.0.0.1 and port 5001 behaves.

Throughout this journey, I gained valuable insights from Stack Overflow, GeeksforGeeks, Real Python, and the Flask documentation, which were all instrumental in overcoming roadblocks and clarifying concepts.

Part 2: Port Scanner

The second component of my Pen Testing Toolkit is a simple Port Scanner. This script allows me to check for open ports on a specified host. I used Python’s built-in socket module to attempt connections to a range of ports. If a connection is successful, it marks the port as open. If not, it silently continues scanning.

This tool gave me practical exposure to how penetration testers identify potential vulnerabilities in a system. Open ports can reveal running services, and each one could be a potential entry point for attackers if not properly secured.

I structured the tool so that I can enter the target IP and port range dynamically. Running this against localhost or even other machines on a LAN helped me see which services were running and which ports were exposed.

By combining both tools the brute forcer and the port scanner I was able to simulate both external reconnaissance (finding open ports) and attack execution (brute-forcing login credentials). This helped me appreciate the full penetration testing workflow from information gathering to exploitation.

Overall, this project pushed me to not only code but also troubleshoot, research, and understand security concepts in depth. This was one of my favourite project I ever created so far and very interesting in security terms.

*OUTPUT*

![Image](https://github.com/user-attachments/assets/6426ff01-719e-4716-b9bc-b8a844fc0006)

![Image](https://github.com/user-attachments/assets/781fb5c4-0219-4633-860e-55c0d31619cf)

![Image](https://github.com/user-attachments/assets/e1e127a3-aa58-4b6a-90c9-ea86a75f7b53)

![Image](https://github.com/user-attachments/assets/14e11c06-eac2-4d5d-8db4-84a34a6596fc)

![Image](https://github.com/user-attachments/assets/055231cc-c4da-4c32-976d-2dbee6e62f14)

![Image](https://github.com/user-attachments/assets/dc2ed813-4136-46e8-a388-3f63c22d08b0)

![Image](https://github.com/user-attachments/assets/9f81e1c4-4397-49c1-92a4-a3ed9f2a5319)
