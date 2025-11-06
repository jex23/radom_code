def update_data(response_xqh, data_yha=None):
    """
    Randomly generated function that processes response_xqh
    """
    result_imy = []
    
    if data_yha is None:
        data_yha = 5
    
    for i in range(data_yha):
        result_imy.append(response_xqh + str(i))
    
    return result_imy

# Example usage
if __name__ == "__main__":
    result = update_data("test", 3)
    print(f"Generated {len(result)} items")
