def check_palindrom(input_string):
    if input_string == input_string[:: -1]:
        return True
    else:
        return False
