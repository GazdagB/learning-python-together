password = input("Enter a password: ")

is_long_enough = len(password) >= 8
has_special_char = "@" in password or "!" in password
has_no_spaces = " " not in password

if is_long_enough and has_special_char and has_no_spaces:
    print("Password is valid")
else:
    print ("Your password is weak")
    
    if not is_long_enough:
        print("Password must be at least 8 characters long")
        
    if not has_special_char:
        print("Password must contain at least one special character (@ or !)")
        
    if not has_no_spaces:
        print("Password must not contain spaces")