# Random Ruby function generated on 2026-02-12

def check_response(items, multiplier = 3)
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
test_data = [45, 52, 72, 12, 66]
result = check_response(test_data)
puts "Processed #{result.length} items"
