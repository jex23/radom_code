# Random Ruby function generated on 2025-09-29

def process_response(items, multiplier = 10)
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
test_data = [73, 86, 77, 64, 100]
result = process_response(test_data)
puts "Processed #{result.length} items"
