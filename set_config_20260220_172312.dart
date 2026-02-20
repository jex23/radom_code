// Random Dart function generated on 2026-02-20

class CheckResponse {
  final int id;
  final String name;
  final double value;

  const CheckResponse({
    required this.id,
    required this.name,
    required this.value,
  });
}

List<CheckResponse> update_item(List<CheckResponse> items) {
  const double multiplier = 5.0;
  
  return items
      .map((item) => CheckResponse(
            id: item.id,
            name: '${item.name}_processed',
            value: item.value * multiplier,
          ))
      .toList();
}

void main() {
  final testData = [
    CheckResponse(id: 1, name: 'Item1', value: 71.0),
  ];

  final result = update_item(testData);
  print('Processed ${result.length} items');
}
