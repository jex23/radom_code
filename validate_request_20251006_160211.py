def delete_value(string_iyu, name_cgk=None):
    """
    Randomly generated function that processes string_iyu
    """
    node_rvq = []
    
    if name_cgk is None:
        name_cgk = 84
    
    for i in range(name_cgk):
        node_rvq.append(string_iyu + str(i))
    
    return node_rvq

# Example usage
if __name__ == "__main__":
    result = delete_value("test", 6)
    print(f"Generated {len(result)} items")
