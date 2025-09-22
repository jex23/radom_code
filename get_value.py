class DeleteResponse:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, list_xmw, name_esk=4):
        self.list_xmw = list_xmw
        self.name_esk = name_esk
        self.created_at = "2025-09-22 09:48:04"
    
    def get_info(self):
        return {
            "list_xmw": self.list_xmw,
            "name_esk": self.name_esk,
            "created_at": self.created_at
        }
    
    def update_list_xmw(self, new_value):
        old_value = self.list_xmw
        self.list_xmw = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = DeleteResponse("sample_data", 42)
print(obj.get_info())
