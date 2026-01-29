// Random Flutter widget generated on 2026-01-29

import 'package:flutter/material.dart';

class ProcessRequest extends StatelessWidget {
  final String title;
  final int value;

  const ProcessRequest({
    Key? key,
    required this.title,
    this.value = 37,
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
