def is_password(password):
    if len(password)<8:
        return False
    has_upper=False
    has_Digits=False
    for char in password:
        if char.isupper():
            has_upper=True
        if char.isdigit():
            has_Digits=True
    if not has_Digits:
        return False
    if not has_upper:
        return False
    return True
print(is_password("kjfdsajh87"))
print(is_password("Ajksdahfhf2"))
print(is_password("ASFDAKLjkfds"))
print(is_password("abcdefghuikj87"))