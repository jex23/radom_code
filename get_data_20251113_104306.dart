// Random Flutter widget generated on 2025-11-13

import 'package:flutter/material.dart';

class SetRequest extends StatelessWidget {
  final String title;
  final int value;

  const SetRequest({
    Key? key,
    required this.title,
    this.value = 78,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.all(16.0),
      child: Column(
        children: [
          Text(title, style: TextStyle(fontSize: 18)),
          Text('Value: $value', style: TextStyle(fontSize: 14)),
        ],
      ),
    );
  }
}
