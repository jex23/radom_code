// Random Flutter widget generated on 2026-02-03

import 'package:flutter/material.dart';

class UpdateUser extends StatelessWidget {
  final String title;
  final int value;

  const UpdateUser({
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
