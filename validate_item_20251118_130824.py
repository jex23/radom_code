def get_result(params_zbf, number_njs=None):
    """
    Randomly generated function that processes params_zbf
    """
    string_jej = []
    
    if number_njs is None:
        number_njs = 94
    
    for i in range(number_njs):
        string_jej.append(params_zbf + str(i))
    
    return string_jej

# Example usage
if __name__ == "__main__":
    result = get_result("test", 1)
    print(f"Generated {len(result)} items")
