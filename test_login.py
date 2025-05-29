from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login_form():
    return '''
    <form method="post" action="/login">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'sanita' and password == 'password123':
        return 'Login successful'
    else:
        return 'Login failed', 401

if __name__ == '__main__':
    app.run(debug=True, port=8080)

