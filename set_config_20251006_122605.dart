// Random Flutter widget generated on 2025-10-06

import 'package:flutter/material.dart';

class HandleRequest extends StatelessWidget {
  final String title;
  final int value;

  const HandleRequest({
    Key? key,
    required this.title,
    this.value = 16,
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
