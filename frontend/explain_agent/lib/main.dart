import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MaterialApp(
    home: FinanceAI(),
  ));
}

class FinanceAI extends StatefulWidget {
  @override
  _FinanceAIState createState() => _FinanceAIState();
}

class _FinanceAIState extends State<FinanceAI> {
  String decision = "Loading...";
  String explanation = "Loading...";

  void fetchData() async {
    final response =
        await http.get(Uri.parse("http://127.0.0.1:5000/decision?symbol=AAPL"));
    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      setState(() {
        decision = data['decision'];
        explanation = data['explanation'];
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("AI Finance Advisor")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text("Decision: $decision",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            SizedBox(height: 20),
            Text("Explanation: $explanation", style: TextStyle(fontSize: 16)),
            SizedBox(height: 30),
            ElevatedButton(onPressed: fetchData, child: Text("Get Decision"))
          ],
        ),
      ),
    );
  }
}
