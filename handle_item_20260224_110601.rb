# Random Ruby function generated on 2026-02-24

def process_response(items, multiplier = 5)
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
test_data = [50, 66, 3, 3, 8]
result = process_response(test_data)
puts "Processed #{result.length} items"
