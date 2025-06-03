def update_data(options_glv, options_xun=None):
    """
    Randomly generated function that processes options_glv
    """
    key_hnb = []
    
    if options_xun is None:
        options_xun = 30
    
    for i in range(options_xun):
        key_hnb.append(options_glv + str(i))
    
    return key_hnb

# Example usage
if __name__ == "__main__":
    result = update_data("test", 8)
    print(f"Generated {len(result)} items")
