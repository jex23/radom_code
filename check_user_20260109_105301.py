class CheckResult:
    """
    A randomly generated class for demonstration
    """
    
    def __init__(self, id_twa, args_zwr=43):
        self.id_twa = id_twa
        self.args_zwr = args_zwr
        self.created_at = "2026-01-09 10:53:01"
    
    def get_info(self):
        return {
            "id_twa": self.id_twa,
            "args_zwr": self.args_zwr,
            "created_at": self.created_at
        }
    
    def update_id_twa(self, new_value):
        old_value = self.id_twa
        self.id_twa = new_value
        return f"Updated from {old_value} to {new_value}"

# Example usage
obj = CheckResult("sample_data", 22)
print(obj.get_info())
