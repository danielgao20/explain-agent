import 'package:flutter/material.dart';
import '../widgets/stock_dropdown.dart';
import '../widgets/stock_chart.dart';
import '../firestore_service.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final FirestoreService _firestoreService = FirestoreService();
  List<String> stockSymbols = [];
  String? selectedStock;
  Map<String, dynamic>? stockData;
  Map<String, dynamic>? analysisData;

  @override
  void initState() {
    super.initState();
    _loadStocks();
  }

  Future<void> _loadStocks() async {
    List<String> symbols = await _firestoreService.getStockSymbols();
    if (symbols.isNotEmpty) {
      setState(() {
        stockSymbols = symbols;
        selectedStock = symbols.first;
      });
      await _loadStockData(selectedStock!);
    }
  }

  Future<void> _loadStockData(String stockSymbol) async {
    setState(() {
      stockData = null;
      analysisData = null;
    });

    Map<String, dynamic>? data =
        await _firestoreService.getStockData(stockSymbol);
    Map<String, dynamic>? analysis =
        await _firestoreService.getStockAnalysis(stockSymbol);

    setState(() {
      stockData = data;
      analysisData = analysis;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFF0D1117), // Dark dark blue background
      appBar: AppBar(
        title:
            Text("Tradegentix Terminal", style: TextStyle(color: Colors.white)),
        backgroundColor: Color(0xFF161B22),
        elevation: 0,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            stockSymbols.isEmpty
                ? Center(
                    child:
                        CircularProgressIndicator(color: Colors.purpleAccent))
                : StockDropdown(
                    stockSymbols: stockSymbols,
                    selectedStock: selectedStock,
                    onStockSelected: (value) {
                      setState(() {
                        selectedStock = value;
                      });
                      _loadStockData(value);
                    },
                  ),
            SizedBox(height: 20),
            Expanded(
              child: stockData == null
                  ? Center(
                      child:
                          CircularProgressIndicator(color: Colors.purpleAccent))
                  : StockPriceChart(
                      stockData: stockData!, analysisData: analysisData),
            ),
          ],
        ),
      ),
    );
  }
}
