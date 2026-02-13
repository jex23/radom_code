class GetResponse:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, status_qdr, node_aiv=83):
        self.status_qdr = status_qdr
        self.node_aiv = node_aiv
        self.created_at = "2026-02-13 16:14:09"
    
    def get_info(self):
        return {
            "status_qdr": self.status_qdr,
            "node_aiv": self.node_aiv,
            "created_at": self.created_at
        }
    
    def update_status_qdr(self, new_value):
        old_value = self.status_qdr
        self.status_qdr = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = GetResponse("sample_data", 36)
print(obj.get_info())
