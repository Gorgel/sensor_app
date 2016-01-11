#include <dht.h>

dht DHT;

#define DHT11_PIN 5

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  // READ DATA
  int chk = DHT.read11(DHT11_PIN);
  String data = "[" + String(DHT.temperature) + "," + String(DHT.humidity) + "]";
  // DISPLAY DATA
  Serial.print(DHT.temperature);
  Serial.print("\n");
  Serial.print(DHT.humidity);
  delay(60000);
}
