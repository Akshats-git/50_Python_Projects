import string
import random
import getpass

def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password is too short. It should be at least 8 characters long.")
    if not any(c.islower() for c in password):
        issues.append("Password should include at least one lowercase letter.")
    if not any(c.isupper() for c in password):
        issues.append("Password should include at least one uppercase letter.")
    if not any(c.isdigit() for c in password):
        issues.append("Password should include at least one digit.")
    if not any(c in string.punctuation for c in password):
        issues.append("Password should include at least one special character.")
    return issues

def generate_strong_password(length = 12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

password = getpass.getpass("Enter your password: ")
issues = check_password_strength(password)
if issues:
    print("Your password has the following issues:")
    for issue in issues:
        print(f"- {issue}")
    suggestion = generate_strong_password()
    print(f"Suggested strong password: {suggestion}")
else:
    print("Your password is Strong!")


    
    
    