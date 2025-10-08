// Random Dart function generated on 2025-10-08

class GetItem {
  final int id;
  final String name;
  final double value;

  const GetItem({
    required this.id,
    required this.name,
    required this.value,
  });
}

List<GetItem> create_data(List<GetItem> items) {
  const double multiplier = 4.0;
  
  return items
      .map((item) => GetItem(
            id: item.id,
            name: '${item.name}_processed',
            value: item.value * multiplier,
          ))
      .toList();
}

void main() {
  final testData = [
    GetItem(id: 1, name: 'Item1', value: 17.0),
  ];

  final result = create_data(testData);
  print('Processed ${result.length} items');
}
