def create_config(node_gux, data_vzs=None):
    """
    Randomly generated function that processes node_gux
    """
    name_afz = []
    
    if data_vzs is None:
        data_vzs = 77
    
    for i in range(data_vzs):
        name_afz.append(node_gux + str(i))
    
    return name_afz

# Example usage
if __name__ == "__main__":
    result = create_config("test", 1)
    print(f"Generated {len(result)} items")
