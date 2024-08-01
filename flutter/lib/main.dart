import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false, // delete debug red line on the right top in app.
      title: 'BBANTO',
      home: Grade(),
    );
  }
}

class Grade extends StatelessWidget {
  const Grade({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.amber[800], // set body bg color
      appBar: AppBar(
        title: Text('BBANTO'),
        backgroundColor: Colors.amber[700], // set bg color to amber color 700
        centerTitle: true,
        elevation: 0.0,
      ),
      body: Padding(
        padding: EdgeInsets.fromLTRB(30.0, 40.0, 0.0, 0.0),
          child: Column(
            // Align all elements of a column widget horizontally
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              // insert image on the top.
              Center(
                child: CircleAvatar( // set image frame
                  backgroundImage: AssetImage('assets/fire.png'),
                  radius: 60.0,
                ),
              ),
              Divider( // make 'divider' between pic and text.
                height: 60.0, // Spacing between the top and bottom widgets
                color: Colors.grey[850],
                thickness: 1.5,
                endIndent: 30.0, // set the margin at the end
              ),
              Text('name',
              style: TextStyle(
                color: Colors.white,
                letterSpacing: 2.0, // set spacing between letters.
            ),
            ),
              SizedBox(
                height: 10.0, // height or width -> blank space
              ),
              Text('BBANTO',
              style: TextStyle(
                color: Colors.white,
                letterSpacing: 2.0,
                fontSize: 28.0,
                fontWeight: FontWeight.bold
              ),
              ),
              SizedBox(
                height: 30.0,
              ),
              Text('BBANTO POWER LEVEL',
                style: TextStyle(
                  color: Colors.white,
                  letterSpacing: 2.0, // set spacing between letters.
                ),
              ),
              SizedBox(
                height: 10.0, // height or width -> blank space
              ),
              Text('14',
                style: TextStyle(
                    color: Colors.white,
                    letterSpacing: 2.0,
                    fontSize: 28.0,
                    fontWeight: FontWeight.bold
                ),
                ),
                SizedBox(
                  height: 30.0,
                ),
                Row(
                  children: <Widget>[
                    Icon(Icons.check_circle_outline),
                    SizedBox(
                      width: 10.0,
                    ),
                    Text('using lightsaber',
                    style: TextStyle(
                      fontSize: 16.0,
                      letterSpacing: 1.0
                    )),
                  ],
                ),
              Row(
                children: <Widget>[
                  Icon(Icons.check_circle_outline),
                  SizedBox(
                    width: 10.0,
                  ),
                  Text('face hero tatoo',
                      style: TextStyle(
                          fontSize: 16.0,
                          letterSpacing: 1.0
                      )),
                ],
              ),
              Row(
                children: <Widget>[
                  Icon(Icons.check_circle_outline),
                  SizedBox(
                    width: 10.0,
                  ),
                  Text('fire flames',
                      style: TextStyle(
                          fontSize: 16.0,
                          letterSpacing: 1.0
                      )),
                ],
              ),
              SizedBox(
                height: 50.0,
              ),
              Center(
                child: CircleAvatar(
                  backgroundImage: AssetImage('assets/dogs.webp'),
                  radius: 40.0,
                  backgroundColor: Colors.amber[800] // like remove bg.
                ),
              )
            ],
          ),
    ),
    );
  }
}

