def check_password_strength(password):
    '''
    Program to check strength of input password
    Parameter:
    password(str): input password
    return:
    output(str): weak or average or strong
    '''

    special_chars = list('@#$%&*')
    isdigit_there = any(char.isdigit() for char in password)
    isupper_there = any(char.isupper() for char in password)
    isspchar_there = any(char in special_chars for char in password)
    check_lower = any(char.islower() for char in password)

    all_true = all([isdigit_there, isupper_there, isspchar_there, check_lower])

    if len(password) < 6:
        return "Weak"
    elif len(password) >= 8 and all_true:
        return "Strong"
    else:
        return "Average"

# Get password input from the user
user_password = input("Enter your password: ")
result = check_password_strength(user_password)
print(f"Password strength: {result}")
