// Random Dart class generated on 2025-09-22

class SetResponse {
  String _name;
  int _value;

  SetResponse(this._name, this._value);

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
