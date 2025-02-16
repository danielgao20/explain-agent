import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';

class StockPriceChart extends StatelessWidget {
  final Map<String, dynamic> stockData;
  final Map<String, dynamic>? analysisData;

  const StockPriceChart(
      {Key? key, required this.stockData, required this.analysisData})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    List<double> bestPath = List<double>.from(stockData["bestPath"] ?? []);
    List<double> bestCase = List<double>.from(stockData["bestCase"] ?? []);

    if (bestPath.isEmpty || bestCase.isEmpty) {
      return Center(
        child: Text("No stock data available.",
            style: TextStyle(color: Colors.white)),
      );
    }

    return Column(
      key: ValueKey(stockData),
      children: [
        Text(
          "Stock Price Projection",
          style: TextStyle(
              fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
        ),
        SizedBox(height: 10),
        Expanded(
          child: Padding(
            padding: const EdgeInsets.all(12.0),
            child: LineChart(
              LineChartData(
                backgroundColor: Color(0xFF161B22),
                gridData: FlGridData(show: false),
                borderData: FlBorderData(
                  border: Border.all(color: Colors.white30),
                ),
                lineBarsData: [
                  // Red Line: Actual Path (bestPath)
                  LineChartBarData(
                    spots: List.generate(
                      bestPath.length,
                      (index) => FlSpot(index.toDouble(), bestPath[index]),
                    ),
                    isCurved: true,
                    color: Colors.redAccent,
                    dotData: FlDotData(show: false),
                    barWidth: 3,
                  ),
                  // Green Line: Predicted Best Case (bestCase)
                  LineChartBarData(
                    spots: List.generate(
                      bestCase.length,
                      (index) => FlSpot(index.toDouble(), bestCase[index]),
                    ),
                    isCurved: true,
                    color: Colors.greenAccent,
                    dotData: FlDotData(
                      show: true,
                      getDotPainter: (spot, percent, barData, index) =>
                          FlDotCirclePainter(
                        radius: 4,
                        color: Colors.purpleAccent,
                        strokeWidth: 2,
                      ),
                    ),
                  ),
                ],
                titlesData: FlTitlesData(
                  leftTitles: AxisTitles(
                    sideTitles: SideTitles(
                      showTitles: true,
                      reservedSize: 40,
                      getTitlesWidget: (value, meta) => Text(
                        value.toStringAsFixed(2), // ✅ Show 2 decimal places
                        style: TextStyle(color: Colors.white, fontSize: 12),
                      ),
                    ),
                  ),
                  bottomTitles: AxisTitles(
                    sideTitles: SideTitles(
                      showTitles: false,
                    ),
                  ),
                ),
              ),
            ),
          ),
        ),
        SizedBox(height: 10),
        analysisData != null
            ? ElevatedButton(
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.purpleAccent,
                  foregroundColor: Colors.white,
                  padding: EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10)),
                ),
                onPressed: () => _showAnalysisDialog(context, analysisData!),
                child: Text("View Analysis"),
              )
            : SizedBox(),
      ],
    );
  }

  void _showAnalysisDialog(
      BuildContext context, Map<String, dynamic> analysisData) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: Color(0xFF161B22),
        title: Text("Stock Analysis", style: TextStyle(color: Colors.white)),
        content: Text(
          analysisData["analysis"] ?? "No analysis available.",
          style: TextStyle(color: Colors.white70),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text("Close", style: TextStyle(color: Colors.purpleAccent)),
          ),
        ],
      ),
    );
  }
}
