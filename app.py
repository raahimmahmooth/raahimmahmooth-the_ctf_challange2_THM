from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

ALLOWED_EMAILS = {
    'asmith@gmail.com': '123456789'
}

LOGIN_SUCCESS_FLAG = 'THM{try_to_find_me}'
RESET_TRIGGER_FLAG = 'THM{reset_path_disclosure}'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email in ALLOWED_EMAILS and ALLOWED_EMAILS[email] == password:
            return render_template('welcome.html', user=email.split('@')[0], flag=LOGIN_SUCCESS_FLAG)
        elif email in ALLOWED_EMAILS and ALLOWED_EMAILS[email] != password:
            return render_template('login.html', error="Invalid Password.")
        else:
            return render_template('login.html', error="Email does not exist.")

    return render_template('login.html')


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    if request.method == 'POST':
        email = request.form.get('email')
        if email in ALLOWED_EMAILS:
            return render_template('reset.html', message=f"Reset link sent to {email}.", flag=RESET_TRIGGER_FLAG)
        else:
            return render_template('reset.html', error="Email not found.")

    return render_template('reset.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
