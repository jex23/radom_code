// Random Flutter widget generated on 2025-06-04

import 'package:flutter/material.dart';

class GetItem extends StatelessWidget {
  final String title;
  final int value;

  const GetItem({
    Key? key,
    required this.title,
    this.value = 60,
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
