import re


def validate_name(name: str) -> bool:
    print("Unpatched validate_name called!")
    
    # Check if the name is empty or None
    if not name:
        return False
    
    if len(name) < 3:
        return False

    # Check for valid characters: letters, spaces, and hyphens
    if not re.match(r'^[a-zA-Z\s-]+$', name):
        return False
    
    # Check for leading/trailing spaces or hyphens
    if name[0] in " -" or name[-1] in " -":
        return False
    
    # Check for consecutive spaces or hyphens
    if re.search(r'\s{2,}', name) or re.search(r'-{2,}', name):
        return False
    
    return True
