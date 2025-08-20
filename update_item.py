def create_response(params_eye, options_ptg=None):
    """
    Randomly generated function that processes params_eye
    """
    element_epc = []
    
    if options_ptg is None:
        options_ptg = 8
    
    for i in range(options_ptg):
        element_epc.append(params_eye + str(i))
    
    return element_epc

# Example usage
if __name__ == "__main__":
    result = create_response("test", 8)
    print(f"Generated {len(result)} items")
