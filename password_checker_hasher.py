import hashlib
import random
import string

def check_password_strength(password):
    """
    Checks the strength of a password using various criteria.
    Returns a score indicating the strength of the password.
    """
    score = 0

    # Length-based scoring
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1

    # Character composition scoring
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>/?`~" for c in password):
        score += 1

    # Additional criteria
    if not password.isnumeric():
        score += 1
    if not any(char.isalpha() for char in password):
        score += 1
    if password.lower() != password and password.upper() != password:
        score += 1
    if any(word in password.lower() for word in ['password', '123456', 'qwerty']):
        score -= 1

    return score

def hash_password(password):
    """
    Hashes a password using the SHA-256 algorithm with a random salt.
    Returns the hashed password and the generated salt.
    """
    salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    hash_object = hashlib.sha256((password + salt).encode())
    hashed_password = hash_object.hexdigest()
    return hashed_password, salt

def validate_password(password):
    """
    Validates a password against specific requirements.
    Returns True if the password is valid, False otherwise.
    """
    if len(password) < 8:
        return False
    # Add more validation criteria if needed
    return True

def save_wordlist(wordlist, filename):
    with open(filename, "w") as file:
        for word in wordlist:
            file.write(word + "\n")

    print(f"\nWordlist generated successfully and saved as '{filename}'.")

def main():
    print("Welcome to the Beginner Cyber Security Program!")
    print("----------------------------------------------")

    while True:
        print("\nPlease choose an option:")
        print("1. Check password strength")
        print("2. Hash a password")
        print("3. Validate a password")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            password = input("Enter a password: ")
            strength = check_password_strength(password)
            print(f"Password strength: {strength} out of 8")

        elif choice == "2":
            password = input("Enter a password: ")
            if validate_password(password):
                hashed_password, salt = hash_password(password)
                print(f"Hashed password: {hashed_password}")
                print(f"Salt: {salt}")
            else:
                print("Invalid password. Password must be at least 8 characters long.")

        elif choice == "3":
            password = input("Enter a password: ")
            if validate_password(password):
                print("Password is valid.")
            else:
                print("Invalid password. Password must be at least 8 characters long.")

        elif choice == "4":
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
