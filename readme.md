# Password Strength Checker and Hasher

This is a simple Python program that allows you to check the strength of a password and hash passwords using the SHA-256 algorithm with a random salt.

## Usage

1. Clone the repository or download the `password_checker_hasher.py` file.

2. Make sure you have Python installed on your system.

3. Open a terminal or command prompt and navigate to the directory where the `password_checker_hasher.py` file is located.

4. Run the script by entering the following command:
   ```
   python password_checker_hasher.py
   ```

5. The program will display a menu with the following options:

   - **Check password strength:** Enter `1` to check the strength of a password. The program will prompt you to enter a password, and it will evaluate the password based on various criteria, such as length, character composition, and additional factors. The program will display a strength score indicating the password's strength.

   - **Hash a password:** Enter `2` to hash a password. The program will prompt you to enter a password, and if the password meets the minimum length requirement (8 characters), it will generate a random salt and hash the password using the SHA-256 algorithm. It will display the hashed password and the generated salt.

   - **Validate a password:** Enter `3` to validate a password. The program will prompt you to enter a password and check if it meets the minimum length requirement (8 characters). It will provide immediate feedback indicating whether the password is valid or invalid.

   - **Exit:** Enter `4` to exit the program.

6. Follow the prompts and enter the necessary information based on your chosen option.

## Additional Features

The program also includes the following features:

- **Wordlist Generation:** The program provides a new option to generate a wordlist. However, this feature requires additional input and is not accessible through the main menu. To use this feature, modify the code accordingly and run the script.

## Security Considerations

- The program uses the SHA-256 algorithm to hash passwords, which is a widely accepted cryptographic hash function. However, for more advanced security, consider using stronger and slower hashing algorithms like bcrypt or Argon2.

- The program generates a random salt for each password, enhancing the security of the hashing process. This ensures that even if two users have the same password, their hashed passwords will be different.

- Please note that this program is intended for educational and informational purposes only. It does not cover all aspects of secure password handling and storage. In a production environment, it is recommended to use established libraries and follow industry best practices for password storage and handling.

Please let me know if you need any further assistance!
