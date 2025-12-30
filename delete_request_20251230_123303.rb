# Random Ruby function generated on 2025-12-30

def check_request(items, multiplier = 3)
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
test_data = [76, 36, 15, 70, 70]
result = check_request(test_data)
puts "Processed #{result.length} items"
