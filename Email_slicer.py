# ask user to input email address
email = input("enter your email address: ")

# slice username 
user = email[:email.index('@')]

# slice domain name
domain = email[email.index("@")+1:]

print("Your User Name is ", user, "your domain is ", domain)
