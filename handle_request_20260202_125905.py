def process_result(result_tmf, name_bdv=None):
    """
    Randomly generated function that processes result_tmf
    """
    response_jdc = []
    
    if name_bdv is None:
        name_bdv = 11
    
    for i in range(name_bdv):
        response_jdc.append(result_tmf + str(i))
    
    return response_jdc

# Example usage
if __name__ == "__main__":
    result = process_result("test", 8)
    print(f"Generated {len(result)} items")
