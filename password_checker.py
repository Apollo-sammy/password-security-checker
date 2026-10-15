"""
Password Security Checker
A beginner-friendly command-line project for checking basic password requirements.
"""

import string


def check_password(password):
    """Return a list of missing requirements and an overall strength rating."""
    missing = []

    if len(password) < 8:
        missing.append("At least 8 characters")

    if not any(char.isupper() for char in password):
        missing.append("At least one uppercase letter (A-Z)")

    if not any(char.islower() for char in password):
        missing.append("At least one lowercase letter (a-z)")

    if not any(char.isdigit() for char in password):
        missing.append("At least one number (0-9)")

    if not any(char in string.punctuation for char in password):
        missing.append("At least one special character (e.g. !, @, #, $)")

    passed = 5 - len(missing)

    if passed <= 2:
        strength = "Weak"
    elif passed <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return missing, strength


def main():
    print("=" * 42)
    print("       PASSWORD SECURITY CHECKER")
    print("=" * 42)
    print("Enter a password to check its basic security.")
    print("Note: this demo checks locally and does not save your password.")
    print()

    password = input("Enter password: ")
    missing, strength = check_password(password)

    print("\n--- PASSWORD CHECK RESULTS ---")
    if missing:
        print("Requirements to improve:")
        for requirement in missing:
            print(f"  [MISSING] {requirement}")
    else:
        print("All basic requirements have been met!")

    print(f"\nOverall strength: {strength}")

    if strength == "Strong":
        print("Good! Your password meets all listed requirements.")
    elif strength == "Medium":
        print("Almost there. Meet the missing requirements to improve it.")
    else:
        print("Try a longer password with different character types.")

    print("\nSecurity tip: use a unique password for every account.")


if __name__ == "__main__":
    main()
