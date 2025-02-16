import 'package:flutter/material.dart';

class StockDropdown extends StatelessWidget {
  final List<String> stockSymbols;
  final String? selectedStock;
  final Function(String) onStockSelected;

  const StockDropdown({
    Key? key,
    required this.stockSymbols,
    required this.selectedStock,
    required this.onStockSelected,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 16),
      decoration: BoxDecoration(
        color: Color(0xFF161B22), // Dark background for dropdown
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: Colors.white38),
      ),
      child: DropdownButtonHideUnderline(
        child: DropdownButton<String>(
          dropdownColor: Color(0xFF161B22), // Dark background for dropdown list
          value: selectedStock,
          icon: Icon(Icons.arrow_drop_down, color: Colors.white),
          style: TextStyle(color: Colors.white, fontSize: 16), // White text
          items: stockSymbols.map((String stock) {
            return DropdownMenuItem<String>(
              value: stock,
              child: Text(stock,
                  style: TextStyle(color: Colors.white)), // Ensure white text
            );
          }).toList(),
          onChanged: (value) {
            if (value != null) {
              onStockSelected(value);
            }
          },
        ),
      ),
    );
  }
}
