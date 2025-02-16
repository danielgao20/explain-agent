import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;

class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    return const FirebaseOptions(
        apiKey: "AIzaSyCs92yI2rS_vSlegySBf_AdPCOpNFM2nxw",
        authDomain: "lighads.firebaseapp.com",
        databaseURL: "https://lighads-default-rtdb.firebaseio.com",
        projectId: "lighads",
        storageBucket: "lighads.firebasestorage.app",
        messagingSenderId: "393408111599",
        appId: "1:393408111599:web:bea3046a44b8dd6fe3cc1a",
        measurementId: "G-GM2X68YZ7Q");
  }
}
