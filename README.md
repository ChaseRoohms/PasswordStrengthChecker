# Password Strength and Validity Checker
This is a simple python script for verifying password strength.

## Password Metrics
The script checks your password for the following:
- REQUIRED:  Contains an upper case letter
- REQUIRED:  Contains a lower case letter
- REQUIRED:  Contains a number
- REQUIRED:  Contains a special character
- REQUIRED:  Length is at least 8
- SUGGESTED: Length is at least 12

The script then cross references your password against a list of the one million most commonly used passwords.

The script then checks your password for any dictionary words.

## Usage
*Clone the repository, and then run the script using the following arguments*

password_strength.py \<password\>
