import re

def get_phone(msg):

    phone = False
    
    regex_pattern = "\\+?[1-9][0-9]{7,14}"
    regex_found = re.findall(regex_pattern, msg)

    if regex_found:
        phone = regex_found[0]

    return phone