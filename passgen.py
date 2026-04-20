import random
import string
import secrets

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    charset = ""
    guaranteed = []

    if use_uppercase:
        charset += string.ascii_uppercase
        guaranteed.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        charset += string.ascii_lowercase
        guaranteed.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        charset += string.digits
        guaranteed.append(secrets.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        charset += symbols
        guaranteed.append(secrets.choice(symbols))

    if not charset:
        return None

    remaining_length = length - len(guaranteed)
    password_chars = guaranteed + [secrets.choice(charset) for _ in range(remaining_length)]
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)

def get_strength(length, pool_size):
    import math
    if pool_size == 0:
        return "N/A"
    entropy = length * math.log2(pool_size)
    if entropy < 28:
        return "Weak"
    elif entropy < 50:
        return "Fair"
    elif entropy < 80:
        return "Good"
    else:
        return "Strong"

def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes"):
            return True
        elif ans in ("n", "no"):
            return False
        else:
            print("  Please enter y or n.")

def main():
    print("=" * 45)
    print("PASSWORD GENERATOR")
    print("=" * 45)

    # Get password length
    while True:
        try:
            length = int(input("\nEnter desired password length (6-64): "))
            if 6 <= length <= 64:
                break
            else:
                print("  Length must be between 6 and 64.")
        except ValueError:
            print("  Please enter a valid number.")

    print("\nChoose character types to include:")
    use_uppercase = get_yes_no("  Uppercase letters (A-Z)? [y/n]: ")
    use_lowercase = get_yes_no("  Lowercase letters (a-z)? [y/n]: ")
    use_digits    = get_yes_no("  Numbers (0-9)?            [y/n]: ")
    use_symbols   = get_yes_no("  Symbols (!@#$...)?        [y/n]: ")

    if not any([use_uppercase, use_lowercase, use_digits, use_symbols]):
        print("\n You must select at least one character type. Exiting.")
        return

    pool = 0
    if use_uppercase: pool += 26
    if use_lowercase: pool += 26
    if use_digits:    pool += 10
    if use_symbols:   pool += 28

    print("\n" + "-" * 45)

    while True:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        strength = get_strength(length, pool)

        print(f"\n Generated Password:\n")
        print(f"   {password}")
        print(f"\n   Length   : {len(password)} characters")
        print(f"   Strength : {strength}")
        print("-" * 45)

        again = get_yes_no("\nGenerate another password with same settings? [y/n]: ")
        if not again:
            break

    print("\nStay secure! \n")

if __name__ == "__main__":
    main()