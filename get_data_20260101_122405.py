class UpdateValue:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, type_ckt, count_ffs=12):
        self.type_ckt = type_ckt
        self.count_ffs = count_ffs
        self.created_at = "2026-01-01 12:24:05"
    
    def get_info(self):
        return {
            "type_ckt": self.type_ckt,
            "count_ffs": self.count_ffs,
            "created_at": self.created_at
        }
    
    def update_type_ckt(self, new_value):
        old_value = self.type_ckt
        self.type_ckt = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = UpdateValue("sample_data", 26)
print(obj.get_info())
