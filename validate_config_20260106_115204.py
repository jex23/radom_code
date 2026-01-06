def handle_request(name_ttp, response_goo=None):
    """
    Randomly generated function that processes name_ttp
    """
    result_rap = []
    
    if response_goo is None:
        response_goo = 22
    
    for i in range(response_goo):
        result_rap.append(name_ttp + str(i))
    
    return result_rap

# Example usage
if __name__ == "__main__":
    result = handle_request("test", 8)
    print(f"Generated {len(result)} items")
