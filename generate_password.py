import string
import random


def generate_password(length):
    """
    Generates a random password with uppercase, lowercase, numbers, and special characters.

    Args:
        length: The desired length of the password.

    Returns:
        A string representing the generated password, or None if the length is too short.
    """

    # Restrict passwords with very small lengths
    if length < 8:
        print("Password length must be at least 8 characters.")
        return None

    # Combine all character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one character from each category
    password = []
    required_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password.extend(required_chars)

    # Fill the rest with random characters
    for _ in range(length - 4):
        password.append(random.choice(characters))

    # Example of using an iteration in join: password_with_just_random_characters = ''.join(random.choice(characters) for _ in range(length))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)


print(generate_password(12))  # Example output: i69D@&,9@czm

