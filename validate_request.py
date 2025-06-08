class ProcessResponse:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, index_ulw, index_dfn=34):
        self.index_ulw = index_ulw
        self.index_dfn = index_dfn
        self.created_at = "2025-06-08 08:01:00"
    
    def get_info(self):
        return {
            "index_ulw": self.index_ulw,
            "index_dfn": self.index_dfn,
            "created_at": self.created_at
        }
    
    def update_index_ulw(self, new_value):
        old_value = self.index_ulw
        self.index_ulw = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = ProcessResponse("sample_data", 16)
print(obj.get_info())
