# Take email address from the user
# Slice it with @ into username and domain
# Slice domain name with . into domain and extension

def main():
    print("Welcome to Email Slicer program")

    email_address = input("Enter your Email address: ")

    (username, domain) = email_address.split("@")
    (domain, extension) = domain.split(".")

    print("Your Username is: ", username)
    print("The Domain name is: ", domain)
    print("The Extension is: ", extension)


main()
