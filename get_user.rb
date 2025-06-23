# Random Ruby class generated on 2025-06-23

class DeleteResponse
  attr_reader :name, :value, :created_at
  attr_writer :name, :value

  def initialize(name, value = 74)
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
obj = DeleteResponse.new("sample", 39)
puts obj.to_hash
