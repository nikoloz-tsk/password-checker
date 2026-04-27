import re
import string

def check_password_strength(password):
    score = 0
    feedback = []

    # length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("⚠️  12+ characters makes it much stronger")

    # uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z)")

    # lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")

    # number check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")

    # special character check
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add a special character (!@#$%^&*...)")

    # common passwords check
    common = ["password", "123456", "qwerty", "abc123", "letmein", "admin"]
    if password.lower() in common:
        score = 0
        feedback.append("❌ This is one of the most common passwords!")

    if score <= 2:
        strength = "🔴 WEAK"
    elif score <= 4:
        strength = "🟡 MODERATE"
    elif score <= 5:
        strength = "🟢 STRONG"
    else:
        strength = "✅ VERY STRONG"

    return strength, score, feedback


def main():
    print("=" * 45)
    print("   🔐 Password Strength Checker")
    print("   Built by Nikoloz Tskhovrebadze")
    print("=" * 45)

    while True:
        password = input("\nEnter a password to check (or 'q' to quit): ")

        if password.lower() == 'q':
            print("\nStay secure! 👋")
            break

        strength, score, feedback = check_password_strength(password)

        print(f"\nStrength: {strength} ({score}/6)")
        print("-" * 35)

        if feedback:
            print("Suggestions:")
            for tip in feedback:
                print(f"  {tip}")
        else:
            print("Great password! No suggestions.")

        print("-" * 35)


if __name__ == "__main__":
    main()