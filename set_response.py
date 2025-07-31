class ProcessResult:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, name_riz, status_ind=86):
        self.name_riz = name_riz
        self.status_ind = status_ind
        self.created_at = "2025-07-31 14:30:35"
    
    def get_info(self):
        return {
            "name_riz": self.name_riz,
            "status_ind": self.status_ind,
            "created_at": self.created_at
        }
    
    def update_name_riz(self, new_value):
        old_value = self.name_riz
        self.name_riz = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = ProcessResult("sample_data", 14)
print(obj.get_info())
