def process_value(item_vif, response_zma=None):
    """
    Randomly generated function that processes item_vif
    """
    config_bju = []
    
    if response_zma is None:
        response_zma = 26
    
    for i in range(response_zma):
        config_bju.append(item_vif + str(i))
    
    return config_bju

# Example usage
if __name__ == "__main__":
    result = process_value("test", 8)
    print(f"Generated {len(result)} items")
