// Random Dart function generated on 2025-12-01

class DeleteUser {
  final int id;
  final String name;
  final double value;

  const DeleteUser({
    required this.id,
    required this.name,
    required this.value,
  });
}

List<DeleteUser> get_user(List<DeleteUser> items) {
  const double multiplier = 9.0;
  
  return items
      .map((item) => DeleteUser(
            id: item.id,
            name: '${item.name}_processed',
            value: item.value * multiplier,
          ))
      .toList();
}

void main() {
  final testData = [
    DeleteUser(id: 1, name: 'Item1', value: 38.0),
  ];

  final result = get_user(testData);
  print('Processed ${result.length} items');
}
