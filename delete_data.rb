# Random Ruby class generated on 2025-06-11

class SetUser
  attr_reader :name, :value, :created_at
  attr_writer :name, :value

  def initialize(name, value = 1)
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
obj = SetUser.new("sample", 28)
puts obj.to_hash
