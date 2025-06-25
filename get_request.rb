# Random Ruby function generated on 2025-06-25

def get_request(items, multiplier = 5)
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
test_data = [37, 40, 94, 14, 1]
result = get_request(test_data)
puts "Processed #{result.length} items"
