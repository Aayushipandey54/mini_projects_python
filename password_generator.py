import random
import string

def generate_password(length=8, use_special=True, use_digits=True, use_uppercase=True):
    """
    Generates a strong random password based on user preferences.

    :param length: The length of the password.
    :param use_special: Whether to include special characters.
    :param use_digits: Whether to include digits.
    :param use_uppercase: Whether to include uppercase letters.
    :return: The generated password as a string.
    """
    # Defining character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""
    
    # Combining the selected character sets
    all_characters = lower + upper + digits + special
    
    if not all_characters:
        raise ValueError("At least one character type should be selected.")

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example Usage
generated_password = generate_password(length=12, use_special=True, use_digits=True, use_uppercase=True)
generated_password
