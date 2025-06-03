# Random Ruby function generated on 2025-06-03

def handle_result(items, multiplier = 6)
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
test_data = [28, 94, 39, 48, 80]
result = handle_result(test_data)
puts "Processed #{result.length} items"
