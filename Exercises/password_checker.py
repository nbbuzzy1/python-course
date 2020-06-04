# Print the username, the password with asterics, and length of the password
username = input('Please enter your username: ')
password = input('Please enter your password: ')
coded_password = '*' * len(password)

print(f'{username} your password {coded_password} is {len(coded_password)} characters long')