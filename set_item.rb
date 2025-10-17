# Random Ruby class generated on 2025-10-17

class ValidateConfig
  attr_reader :name, :value, :created_at
  attr_writer :name, :value

  def initialize(name, value = 28)
    @name = name
    @value = value
    @created_at = Time.now
  end

  def to_hash
    {
      name: @name,
      value: @value,
      created_at: @created_at.iso8601
    }
  end

  def update_value(new_value)
    old_value = @value
    @value = new_value
    "Updated from #{old_value} to #{new_value}"
  end
end

# Example usage
obj = ValidateConfig.new("sample", 16)
puts obj.to_hash
