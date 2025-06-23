def delete_value(id_ocn, element_dyr=None):
    """
    Randomly generated function that processes id_ocn
    """
    response_frf = []
    
    if element_dyr is None:
        element_dyr = 52
    
    for i in range(element_dyr):
        response_frf.append(id_ocn + str(i))
    
    return response_frf

# Example usage
if __name__ == "__main__":
    result = delete_value("test", 8)
    print(f"Generated {len(result)} items")
