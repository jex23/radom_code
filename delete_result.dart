// Random Dart function generated on 2025-06-09

class GetUser {
  final int id;
  final String name;
  final double value;

  const GetUser({
    required this.id,
    required this.name,
    required this.value,
  });
}

List<GetUser> check_value(List<GetUser> items) {
  const double multiplier = 5.0;
  
  return items
      .map((item) => GetUser(
            id: item.id,
            name: '${item.name}_processed',
            value: item.value * multiplier,
          ))
      .toList();
}

void main() {
  final testData = [
    GetUser(id: 1, name: 'Item1', value: 15.0),
  ];

  final result = check_value(testData);
  print('Processed ${result.length} items');
}
