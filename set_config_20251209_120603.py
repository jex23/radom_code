def update_item(count_pmm, id_gsw=None):
    """
    Randomly generated function that processes count_pmm
    """
    string_cvh = []
    
    if id_gsw is None:
        id_gsw = 98
    
    for i in range(id_gsw):
        string_cvh.append(count_pmm + str(i))
    
    return string_cvh

# Example usage
if __name__ == "__main__":
    result = update_item("test", 8)
    print(f"Generated {len(result)} items")
