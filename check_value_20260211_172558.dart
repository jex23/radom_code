// Random Dart function generated on 2026-02-11

class DeleteRequest {
  final int id;
  final String name;
  final double value;

  const DeleteRequest({
    required this.id,
    required this.name,
    required this.value,
  });
}

List<DeleteRequest> delete_value(List<DeleteRequest> items) {
  const double multiplier = 8.0;
  
  return items
      .map((item) => DeleteRequest(
            id: item.id,
            name: '${item.name}_processed',
            value: item.value * multiplier,
          ))
      .toList();
}

void main() {
  final testData = [
    DeleteRequest(id: 1, name: 'Item1', value: 46.0),
  ];

  final result = delete_value(testData);
  print('Processed ${result.length} items');
}
