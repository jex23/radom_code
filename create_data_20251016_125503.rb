# Random Ruby function generated on 2025-10-16

def process_data(items, multiplier = 8)
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
test_data = [75, 58, 53, 2, 64]
result = process_data(test_data)
puts "Processed #{result.length} items"
