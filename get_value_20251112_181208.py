def update_item(type_gxt, element_rxr=None):
    """
    Randomly generated function that processes type_gxt
    """
    name_eol = []
    
    if element_rxr is None:
        element_rxr = 48
    
    for i in range(element_rxr):
        name_eol.append(type_gxt + str(i))
    
    return name_eol

# Example usage
if __name__ == "__main__":
    result = update_item("test", 8)
    print(f"Generated {len(result)} items")
