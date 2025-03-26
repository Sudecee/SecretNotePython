This exploit is a simple sql injection attack written for ethical hackers like me. Please do not use it for malicious purposes.

This script is a basic SQL Injection PoC that attempts to bypass authentication on a vulnerable website.
It takes a target URL as an argument and sends a POST request with an SQL Injection payload in the username field

How It Works (SQL Injection PoC):
1-Takes the target URL from the command-line argument.

2-Sends a POST request with the SQLi payload as the username and a dummy password.

3-Checks the response for success indicators like "Welcome" or "Success".

4-Prints the result: If successful, it means the login was bypassed; otherwise, the attack failed.
