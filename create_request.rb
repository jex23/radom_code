# Random Ruby function generated on 2025-07-05

def validate_response(items, multiplier = 5)
  return [] if items.nil? || items.empty?
  
  items.map.with_index do |item, index|
    {
      original: item,
      processed: item * multiplier,
      index: index,
      timestamp: Time.now.iso8601
    }
  end
end

# Example usage
test_data = [45, 90, 72, 2, 76]
result = validate_response(test_data)
puts "Processed #{result.length} items"
