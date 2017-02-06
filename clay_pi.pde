// screen resolution for pi and 7inch LCD touch screen

String otherName = "";
String displayed ="";
String displayed2 ="";
String lines[];
String right = " // // // ";
String left = " \\ \\ \\ ";
int index;
int i = 0;
PImage img;

int interval = 12; // 2s
int time;
String c;

PFont font;

void setup() {
  fullScreen();
  font = createFont("arial", 56);
  background(0);
  img = loadImage("/home/pi/clay_prayers/claycam.jpg");
  displayed = "";
  displayed2 = "";
  time = millis();
  textFont(font);
  fill(0, 0, 0);
  String lines[] = loadStrings("/home/pi/clay_prayers/clay1.txt");
  c = "1";
}

void draw() {
  background(255, 255, 255);
  text(displayed, 100, 100, 600, 300);
  textAlign(CENTER, CENTER);
  String lines[] = loadStrings("/home/pi/clay_prayers/clay1.txt");
  if (lines.length > 0){
      displayed = lines[0];
      //time  = millis() + millis()/2;
      c = "0";
  }
  else {
    //delay (500);
    if (c == "0"){
      if(i < 20) {
             imageMode(CORNER);
    	       image(img, 80, 40, 600, 410);
             i ++;
                  }
      if (i == 20){
      	           i = 0;
                   c = "1";
      }
    }
     else {
	       displayed = right;
           } 
    }
  }
