
// screen resolution for pi and 7inch LCD touch screen
float angle;
float jitter;
String otherName = "";
String displayed ="";
String displayed2 ="";
String lines[];
String right = " // // // ";
String left = " \\ \\ \\ ";
int index;
int i = 0;
PImage img;
int pic = 1;
int interval = 12; // 2s
int time;
String c;
int side;

PFont font;
PFont code;

void setup() {

  //noStroke();
  fill(255, 255, 255);
  rectMode(CENTER);

  fullScreen();
  font = createFont("roboto", 56);
  code = createFont("arial", 10);
  background(0);
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
  text(displayed, 400, 200, 600, 300);
  textFont(font);
  textAlign(CENTER, CENTER);
  String lines[] = loadStrings("/home/pi/clay_prayers/clay1.txt");
  if (lines.length > 0){
      displayed = lines[0];
      //time  = millis() + millis()/2;
      c = "0";
      pic = 1;
  }
  else {
    //delay (500);
    if (c == "0"){
      if(i < 20) {
             if(pic == 1){
             delay (2000);
             pic = 0;
             }
             else{
             img = loadImage("/home/pi/clay_prayers/claycam.jpg");
             imageMode(CORNER);
               image(img, 90, 40, 610, 410);
             i ++;
                  }
      }
      if (i == 20){
                   i = 0;
                   c = "1";
      }
    }
     else {
           displayed = "";
            // during even-numbered seconds (0, 2, 4, 6...)
  	   if (second() % 10 == 0) {
           String pic[]  = loadStrings("/home/pi/clay_prayers/claycam.jpg");
           float r = random(0, 100);
           int ran = int(r);
           textFont(code);
           displayed = pic[ran];
           }
	 }
     }
}
