import re

password_rules = [
    "Your password doesn't have at least 8 characters.",
    "Your password doesn't have any special characters.",
    "Your password doesn't have any uppercase letter.",
    "Your password doesn't have any lowercase letter.",
    "Your password doesn't have any numerical digits."
]

def check_password_strength(password):
    conditions = [0, 1, 2, 3, 4]
    strength = 0

    if len(password) >= 8:
        strength += 1
        conditions.remove(0)
    
    if re.search(r'[\W_]', password):
        strength += 1
        conditions.remove(1)
    
    if re.search(r'[A-Z]', password):
        strength += 1
        conditions.remove(2)

    if re.search(r'[a-z]', password):
        strength += 1
        conditions.remove(3)
    
    if re.search(r'[0-9]', password):
        strength += 1
        conditions.remove(4)

    print(f"In the range of 1 to 5, your password strength is: {strength}")
    for i in conditions:
        print(f"Since: {password_rules[i]}")

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    check_password_strength(user_password)
