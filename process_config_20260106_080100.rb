# Random Ruby function generated on 2026-01-06

def handle_item(items, multiplier = 2)
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
test_data = [55, 22, 38, 73, 66]
result = handle_item(test_data)
puts "Processed #{result.length} items"
