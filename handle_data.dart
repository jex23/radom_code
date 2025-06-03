// Random Flutter widget generated on 2025-06-03

import 'package:flutter/material.dart';

class ProcessData extends StatelessWidget {
  final String title;
  final int value;

  const ProcessData({
    Key? key,
    required this.title,
    this.value = 39,
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
