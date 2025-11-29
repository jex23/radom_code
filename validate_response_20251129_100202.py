def get_item(response_rgl, list_fvg=None):
    """
    Randomly generated function that processes response_rgl
    """
    id_rai = []
    
    if list_fvg is None:
        list_fvg = 42
    
    for i in range(list_fvg):
        id_rai.append(response_rgl + str(i))
    
    return id_rai

# Example usage
if __name__ == "__main__":
    result = get_item("test", 5)
    print(f"Generated {len(result)} items")
