
String otherName = "";
String displayed ="";
String displayed2 ="";
String lines[];
String right = " // // // ";
String left = " \\ \\ \\ ";
int index;
int i = 0;

int interval = 12; // 2s
int time;

PFont font;

void setup() {
  fullScreen();
  font = createFont("arial", 56);
  background(0);
  displayed = "";
  displayed2 = "";
  time = millis();
  textFont(font);
  fill(0, 0, 0);
  String lines[] = loadStrings("/home/pi/clay_prayers/clay1.txt");
}

void draw() {
  background(255, 255, 255);
  text(displayed, width/2 - textWidth(displayed)/2, height/2);
  String lines[] = loadStrings("/home/pi/clay_prayers/clay1.txt");
  if (lines.length > 0){
      displayed = lines[0];
      time  = millis() + millis()/2;
  }
  else {
    delay (500);
    displayed = right;
    }
 }

