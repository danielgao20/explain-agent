import 'package:cloud_firestore/cloud_firestore.dart';

class FirestoreService {
  final FirebaseFirestore _db = FirebaseFirestore.instance;

  /// Fetch all stock symbols from Firestore "users" collection
  Future<List<String>> getStockSymbols() async {
    try {
      QuerySnapshot querySnapshot = await _db.collection("users").get();
      return querySnapshot.docs.map((doc) => doc.id).toList();
    } catch (e) {
      print("🔥 Error fetching stock symbols: $e");
      return [];
    }
  }

  /// Fetch stock data from Firestore
  Future<Map<String, dynamic>?> getStockData(String stockSymbol) async {
    try {
      DocumentSnapshot doc =
          await _db.collection("users").doc(stockSymbol).get();
      return doc.exists ? doc.data() as Map<String, dynamic> : null;
    } catch (e) {
      print("🔥 Error fetching stock data: $e");
      return null;
    }
  }

  /// Fetch analysis data from Firestore
  Future<Map<String, dynamic>?> getStockAnalysis(String stockSymbol) async {
    try {
      DocumentSnapshot doc =
          await _db.collection("analysis").doc(stockSymbol).get();
      return doc.exists ? doc.data() as Map<String, dynamic> : null;
    } catch (e) {
      print("🔥 Error fetching analysis: $e");
      return null;
    }
  }
}
