// Random Flutter widget generated on 2025-10-03

import 'package:flutter/material.dart';

class HandleResult extends StatelessWidget {
  final String title;
  final int value;

  const HandleResult({
    Key? key,
    required this.title,
    this.value = 11,
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
