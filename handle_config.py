def check_value(number_lbh, data_vsz=None):
    """
    Randomly generated function that processes number_lbh
    """
    data_udr = []
    
    if data_vsz is None:
        data_vsz = 99
    
    for i in range(data_vsz):
        data_udr.append(number_lbh + str(i))
    
    return data_udr

# Example usage
if __name__ == "__main__":
    result = check_value("test", 2)
    print(f"Generated {len(result)} items")
