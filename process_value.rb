# Random Ruby function generated on 2025-10-28

def get_response(items, multiplier = 10)
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
test_data = [100, 19, 7, 5, 61]
result = get_response(test_data)
puts "Processed #{result.length} items"
