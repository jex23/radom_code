# Random Ruby function generated on 2025-06-03

def process_request(items, multiplier = 2)
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
test_data = [87, 37, 4, 63, 7]
result = process_request(test_data)
puts "Processed #{result.length} items"
