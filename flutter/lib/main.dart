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
    home: MyHomePage(),
    );
  }
}
// MyHomePage 위젯 만들기
class MyHomePage extends StatelessWidget {
  const MyHomePage({super.key});

  @override
  Widget build(BuildContext context) {
    // 앱 화면에 위젯을 보여주기 위한 도화지 역할 Scaffold
    return Scaffold(
      appBar: AppBar(
        title: Text('First App'),
      ),
      // 화면을 만드는 시작점
      body: Center( // 배열을 지정하고 자식들이 있음.
        child: Column(
          children: <Widget>[
            Text('Hello'),
            Text('Hello'),
            Text('Hello')
          ],
        ),
      ),
    );
  }
}
