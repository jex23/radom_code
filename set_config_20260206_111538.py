class ProcessValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, type_ikg, response_ijv=84):
        self.type_ikg = type_ikg
        self.response_ijv = response_ijv
        self.created_at = "2026-02-06 11:15:38"
    
    def get_info(self):
        return {
            "type_ikg": self.type_ikg,
            "response_ijv": self.response_ijv,
            "created_at": self.created_at
        }
    
    def update_type_ikg(self, new_value):
        old_value = self.type_ikg
        self.type_ikg = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = ProcessValue("sample_data", 28)
print(obj.get_info())
