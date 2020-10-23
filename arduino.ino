int button = 2;
int yAxis  = A0;

int const DOWN = 1;
int const UP   = 2;
int const NONE = 0;     

void setup() 
{
  pinMode (button, INPUT_PULLUP);
  
  Serial.begin(9600);
}

void loop() 
{
  if ((analogRead(yAxis)) < 450)
    Serial.println(DOWN);
  else if ((analogRead(yAxis)) > 550)
    Serial.println(UP);
  else 
    Serial.println(NONE); 

  delay(100); 
}
