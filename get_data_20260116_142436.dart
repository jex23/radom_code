// Random Dart class generated on 2026-01-16

class CheckResponse {
  String _name;
  int _value;

  CheckResponse(this._name, this._value);

  String get name => _name;
  int get value => _value;

  set name(String newName) {
    _name = newName;
  }

  set value(int newValue) {
    _value = newValue;
  }

  Map<String, dynamic> toJson() {
    return {
      'name': _name,
      'value': _value,
    };
  }
}
