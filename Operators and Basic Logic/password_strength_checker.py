def password_strength_checker():
    import re
    import math
    import getpass

    try:
        print("=== Password Strength Checker ===")
        print("(Your input will be hidden for security.)")

        password = getpass.getpass("Enter your password: ").strip()

        if not password:
            raise ValueError("Password cannot be empty!")

        # Character sets and scoring rules
        SPECIAL_CHARS = r"""~`!@#$%^&*()-_=+[{]}\|;:'",<.>/?"""
        COMMON_PASSWORDS = {
            "password", "123456", "12345678", "qwerty", "abc123",
            "letmein", "111111", "iloveyou", "admin", "welcome"
        }

        score = 0
        suggestions = []

        # Length check
        if len(password) >= 8:
            score += 1
        else:
            suggestions.append("Use at least 8 characters (12+ recommended).")

        # Lowercase
        if re.search(r"[a-z]", password):
            score += 1
        else:
            suggestions.append("Add lowercase letters.")

        #  Uppercase
        if re.search(r"[A-Z]", password):
            score += 1
        else:
            suggestions.append("Add uppercase letters.")

        #  Numbers
        if re.search(r"[0-9]", password):
            score += 1
        else:
            suggestions.append("Add digits (0-9).")

        #  Special characters
        if re.search(rf"[{re.escape(SPECIAL_CHARS)}]", password):
            score += 1
        else:
            suggestions.append("Add special characters like !@#$%&.")

        #  Common password check
        if password.lower() in COMMON_PASSWORDS:
            score -= 2
            suggestions.append(
                "Avoid common passwords like '123456' or 'password'.")

        #  Repeated character pattern check
        if re.search(r"(.)\1\1", password):
            score -= 1
            suggestions.append(
                "Avoid repeating the same character more than twice (e.g., 'aaa').")

        #  Simple sequence check
        if re.search(r"(abc|123|qwe|xyz)", password.lower()):
            score -= 1
            suggestions.append(
                "Avoid sequential patterns like 'abc' or '123'.")

        #  Entropy estimation (approx.)
        pool = 0
        if re.search(r"[a-z]", password):
            pool += 26
        if re.search(r"[A-Z]", password):
            pool += 26
        if re.search(r"[0-9]", password):
            pool += 10
        if re.search(rf"[{re.escape(SPECIAL_CHARS)}]", password):
            pool += len(SPECIAL_CHARS)
        pool = max(pool, 1)
        entropy = len(password) * math.log2(pool)

        #  Strength verdict
        if score <= 1:
            verdict = "Very Weak"
        elif score == 2:
            verdict = "Weak"
        elif score == 3:
            verdict = "Moderate"
        elif score == 4:
            verdict = "Strong"
        else:
            verdict = "Very Strong"

        print("\n=== Password Strength Report ===")
        print(f"Length: {len(password)}")
        print(f"Score: {score}/5")
        print(f"Entropy: {entropy:.2f} bits")
        print(f"Verdict: {verdict}")

        if suggestions:
            print("\nSuggestions:")
            for s in suggestions:
                print(f" - {s}")
        else:
            print("\nNo suggestions — your password is very strong!")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
if __name__ == "__main__":
    password_strength_checker()
