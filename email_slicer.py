email = input("Enter your email here:")
#find the position of the @ symbol
at_index = email.index("@")
#everything before @ is the username
username = email[:at_index]
#everything after @ is the domain
domain = email[at_index + 1:]
print(f"Your username is: {username}")
print(f"Your domain is: {domain}")




