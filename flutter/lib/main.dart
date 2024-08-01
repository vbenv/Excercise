import 'package:flutter/material.dart'; // 일관된 디자인을 위해 구글에서 제공하는 라이브러리.무조건 이것부터 import

// main함수는 앱의 시작점.
// runapp : 시작하는 최상위 함수. 위젯을 argument로 무조건 가져야 함.
void main() => runApp(MyApp());

// stl 누르면
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // 앱을 총칭하는 이름 <-> 홈 위젯에서의 title은 화면에서 보여지는 text.
      title: 'First app',
      theme: ThemeData(
          primarySwatch: Colors.blue // 색상 견본을 지정하여 기본 색상으로 사용하겠다.
      ),
    // 앱이 정상적으로 실행되었으 때 가장 먼저 보여지는 곳
    home: MyCard(),
    );
  }
}
// MyHomePage 위젯 만들기
class MyCard extends StatelessWidget {
  const MyCard({super.key});

  @override
  Widget build(BuildContext context) {
    //
    return Scaffold(
      appBar: AppBar(
        title: Text('First App'),
        // set title's position.
        centerTitle: true,
        // set background color.
        backgroundColor: Colors.redAccent,
        // appbar elevation.
        elevation: 0.0,
      ),
      body: Center(
        child: Column( // Center + Column : set horizontal axis.
            mainAxisAlignment: MainAxisAlignment.center, // vertical axis
            children: <Widget>[
              Text('Hello'),
              Text('Hello'),
              Text('Hello'),
            ],
          ),
      ),
    );
  }
}
