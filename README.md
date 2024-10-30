# Skellies
- Skellies is a Python script that generates a series of unique hex-based email addresses and strong passwords.
- This tool is useful for creating disposable email accounts for various online services, enhancing privacy and security.
## Features
- Generate a specified number of hex-based email addresses.
- Create strong, random passwords.
- Support for multiple email providers: Gmail, Yahoo, Outlook, and ProtonMail.
- Option to use a single email provider for all generated accounts.
## Usage
- Follow the prompts:
  1. Enter the number of email/password combinations you wish to generate.
  2. Specify the desired length of the password.
  3. Choose whether you want all accounts to be associated with the same email provider.
  4. Select an email provider from the available options.
  5. Specify the desired length of the hexname portion of the email.
> [!NOTE]
> Generated email addresses and passwords will be saved to skellies.txt.
### Example
```bash
Welcome to Skellies!
How many skellies do you want? 5
Desired length of the password: 12
Do you want all the skellies for the same email provider? (yes/no): yes
Choose an email from this list:
 ['gmail', 'yahoo', 'outlook', 'proton']
Email: gmail
Desired length of the hexname? 8

Output

The generated email addresses and passwords will be saved in a file called skellies.txt, in the following format:

Email: 4f3c1a2b@gmail.com, Password: s3cureP@ssw0rd!
Email: a9d3b2e0@gmail.com, Password: anotherP@ssw0rd!
```
