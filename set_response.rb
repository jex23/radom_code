# Random Ruby class generated on 2025-06-10

class HandleResult
  attr_reader :name, :value, :created_at
  attr_writer :name, :value

  def initialize(name, value = 27)
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
obj = HandleResult.new("sample", 48)
puts obj.to_hash
