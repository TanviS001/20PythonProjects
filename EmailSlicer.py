# Take email address from the user
# Slice it with @ into username and domain
# Slice domain name with . into domain and extension

def main():
    print("Welcome to Email Slicer program")

    email_address = input("Enter your Email address: ")

    (username, domain) = email_address.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain name: ", domain)
    print("Extension: ", extension)


main()
