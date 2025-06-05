def parse_measurement(value):
    """Helper function to parse a measurement with optional units.
    dimensions are in cm
    mass is in kg
    """
    if isinstance(value, str):
        value = value.strip()
        if value.endswith("cm"):
            return float(value[:-2].strip())
        elif value.endswith("kg"):
            return float(value[:-2].strip())
    return float(value)

def sort(width, height, length, mass):
    """
    Sort packages into different stacks based on their dimensions and mass.
    
    Args:
        width: Width of the package in cm (float or int)
        height: Height of the package in cm (float or int)
        length: Length of the package in cm (float or int)
        mass: Mass of the package in kg (float or int)
    
    Returns:
        str: The stack where the package should go:
             - "STANDARD" if the package is neither bulky nor heavy.
             - "SPECIAL" if the package is either bulky or heavy.
             - "REJECTED" if the package is both bulky and heavy.
             - "REJECTED" if any input is invalid (None, negative, or non-numeric).
    """
    try:
        # input validation and error handling
  
        # if any of the dimensions are None, return rejected
        # this accounts for edge cases where the dimensions are not provided
        if any(dim is None for dim in [width, height, length, mass]):
            return "REJECTED"

        width = parse_measurement(width)
        height = parse_measurement(height)
        length = parse_measurement(length)
        mass = parse_measurement(mass)

        # returning rejected if any dimensions are negative or zero. since there's no boxes with 0 dimensions
        # Not defined in the rules but accounts for edge cases
        # and return a response that the the automation can handle. potentially add a way to notfiy us of this
        if any(dim <= 0 for dim in [width, height, length, mass]):
            return "REJECTED" 

        # calculate volume
        volume = width * height * length
        # find the largest dimension
        dimensions = max(width, height, length)

       
        is_bulky = volume >= 1000000 or dimensions >= 150
        is_heavy = mass >= 20
       
        if is_bulky and is_heavy:
            return "REJECTED"
        elif is_bulky or is_heavy:
            return "SPECIAL"
        else:
            return "STANDARD"
    except (ValueError, TypeError):
        # returning rejected if any dimensions are not numbers. Not defined in the rules but accounts for edge cases
        # and return a response that the the automation can handle. potentially add a way to notfiy us of this
        return "REJECTED"


