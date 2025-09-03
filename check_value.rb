# Random Ruby function generated on 2025-09-03

def validate_request(items, multiplier = 7)
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
test_data = [33, 18, 72, 53, 90]
result = validate_request(test_data)
puts "Processed #{result.length} items"
