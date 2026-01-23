# Random Ruby function generated on 2026-01-23

def handle_response(items, multiplier = 6)
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
test_data = [23, 84, 79, 54, 55]
result = handle_response(test_data)
puts "Processed #{result.length} items"
