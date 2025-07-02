// Random Dart function generated on 2025-07-02

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

List<GetUser> create_request(List<GetUser> items) {
  const double multiplier = 3.0;
  
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
    GetUser(id: 1, name: 'Item1', value: 21.0),
  ];

  final result = create_request(testData);
  print('Processed ${result.length} items');
}
