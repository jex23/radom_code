// Random Dart function generated on 2025-09-10

class UpdateRequest {
  final int id;
  final String name;
  final double value;

  const UpdateRequest({
    required this.id,
    required this.name,
    required this.value,
  });
}

List<UpdateRequest> update_item(List<UpdateRequest> items) {
  const double multiplier = 5.0;
  
  return items
      .map((item) => UpdateRequest(
            id: item.id,
            name: '${item.name}_processed',
            value: item.value * multiplier,
          ))
      .toList();
}

void main() {
  final testData = [
    UpdateRequest(id: 1, name: 'Item1', value: 56.0),
  ];

  final result = update_item(testData);
  print('Processed ${result.length} items');
}
