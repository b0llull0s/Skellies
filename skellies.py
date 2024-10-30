import secrets
import string
import os

# Banner
banner = '''
      .. ..',..''''','',,,,,,,,,,',,,,'.,,',,,,,,;,,,,,,,,,,,,'.',,'.  ...
       .   ..'...'.,'''''',,;;;,,,,;,,''.',';,,,;;;;;,,,,,,'......,'.    ..
            .'..'..'',,;,;;;;;;;,;;;,,.';;;',;;;;:;;;;;;;,,...''';,.   .
             .....'''''''''''''''''''..''''.'''''''''''''''''.....'.
            .,;;:;;::::;,,,'''.'',;;::;;;;::::;,,'',;;;;:::::;;;;;'.    ....
           .',,,''',,,,','.. .......',''',,,''''.....''',,,,,'',,,'.    ....
           ....''.....            . .',,','..... .   ........'',,,''.     .
            ... .                   ..';;;.....                .'''..
            .                         .........                    .
         .'.                          ..'......                    ...
         ',.           ...     ..    .;,,,'.'..              ..     ''
         .'            ...         .'','''.','.                     ...
        .',.    ........'.  .    .,;,. ..  .:;,'.       ....        .,'  
        ..''.   ...'.......... ..','.       .''''.   .........      ....
       .....,,.....'......'....,,,;.         .''',,............    .',..
      .';,. ..''''''..',;,;,,.'',,'          .......''','........''''..'
   ....,,''..   ......',''..   .'.             ..........''...'.......''.
   ...',;,,...      ..,,;;'.. .;.              .....,,,'.'.. ......';;;:,....
       .....          ....,,....                .'.','''..      ...''''.. ..
        ...   . ..       .,,..''                .'.,;,'..    ...  ...,.
               ............;,.,,.       ..      ''',,....  ...'.....'..
                    .........'''.      .'.     ..''.... ........   ..
                     ...''.';:;;;;'...;:;,'....;':;,','  .;,..                  
'''
print(banner)
# Colors for styling
class bcolors:
    PURPLE='\033[95m'
    BLUE='\033[94m'
    RED='\033[91m'
    ENDC='\033[0m'

## Variables ##
hex_characters='0123456789abcdef'
email_list=["gmail","yahoo","outlook","proton"]

## Functions ##

def generate_hex_email(email, hexname_length):
    hexname=''.join(secrets.choice(hex_characters) for _ in range(hexname_length))
    if email=="proton":
        return f"{hexname}@{email}.me"
    else:
        return f"{hexname}@{email}.com"
     
def generate_password(password_length):
    all_characters=string.ascii_letters+string.digits+string.punctuation
    return ''.join(secrets.choice(all_characters) for _ in range(password_length))
 
def write_to_file(data):
    with open("skellies.txt", "a") as file:
        file.write(data+"\n")
     
## Loop ##
while True:
    try:
        print(bcolors.PURPLE+"Welcome to Skellies!"+bcolors.ENDC)
        num_combinations=int(input(bcolors.PURPLE+"How many skellies do you want? "+bcolors.ENDC))
        if num_combinations<1:
            print(bcolors.RED+"Invalid number of combinations."+bcolors.ENDC)
            continue
        
        password_length=int(input(bcolors.PURPLE+"Desired length of the password: "+bcolors.ENDC))
        repeat_email=input(bcolors.PURPLE+"Do you want all the skellies for the same email provider? (yes/no): "+bcolors.ENDC).lower()=="yes"
        
        if repeat_email:
            print("Choose an email from this list:\n", email_list)
            email=input(bcolors.PURPLE+"Email: "+bcolors.ENDC).lower()
            if email not in email_list:
                print(bcolors.RED+"Invalid email provider chosen."+bcolors.ENDC)
                continue
            hexname_length=int(input(bcolors.PURPLE+"Desired length of the hexname? "+bcolors.ENDC))
            email=email.split('@')[0]  # Resetting email to the original provider
            for _ in range(num_combinations):
                email_with_hexname=generate_hex_email(email,hexname_length)
                write_to_file(f"Email:{email_with_hexname},Password:{generate_password(password_length)}")
        else:
            for _ in range(num_combinations):
                print("Choose an email from this list:\n",email_list)
                email=input(bcolors.PURPLE+"Email: "+bcolors.ENDC).lower()
                if email not in email_list:
                    print(bcolors.RED+"Invalid email provider chosen."+bcolors.ENDC)
                    continue
                hexname_length=int(input(bcolors.PURPLE+"Desired length of the hexname? "+bcolors.ENDC))
                email_with_hexname=generate_hex_email(email,hexname_length)
                write_to_file(f"Email:{email_with_hexname},Password:{generate_password(password_length)}")
                print(bcolors.PURPLE+"Skeleton Raised!"+bcolors.ENDC)
        
        another_round=input(bcolors.PURPLE+"Do you want to raise more skeletons? (y/n): "+bcolors.ENDC).lower()
        if another_round !="y":
            break
    except ValueError:
        print(bcolors.RED+"Please enter a valid number."+bcolors.ENDC)
