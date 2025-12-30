// Random Dart class generated on 2025-12-30

class CreateResponse {
  String _name;
  int _value;

  CreateResponse(this._name, this._value);

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
