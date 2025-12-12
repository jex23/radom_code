def get_response(data_npg, response_gql=None):
    """
    Randomly generated function that processes data_npg
    """
    index_uiu = []
    
    if response_gql is None:
        response_gql = 64
    
    for i in range(response_gql):
        index_uiu.append(data_npg + str(i))
    
    return index_uiu

# Example usage
if __name__ == "__main__":
    result = get_response("test", 4)
    print(f"Generated {len(result)} items")
