class CheckConfig:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, status_raq, index_fil=58):
        self.status_raq = status_raq
        self.index_fil = index_fil
        self.created_at = "2025-08-19 12:38:06"
    
    def get_info(self):
        return {
            "status_raq": self.status_raq,
            "index_fil": self.index_fil,
            "created_at": self.created_at
        }
    
    def update_status_raq(self, new_value):
        old_value = self.status_raq
        self.status_raq = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CheckConfig("sample_data", 30)
print(obj.get_info())
