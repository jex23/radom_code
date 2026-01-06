def check_request(type_ooe, request_zlw=None):
    """
    Randomly generated function that processes type_ooe
    """
    number_bfc = []
    
    if request_zlw is None:
        request_zlw = 51
    
    for i in range(request_zlw):
        number_bfc.append(type_ooe + str(i))
    
    return number_bfc

# Example usage
if __name__ == "__main__":
    result = check_request("test", 6)
    print(f"Generated {len(result)} items")
