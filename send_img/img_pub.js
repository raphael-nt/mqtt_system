const fs = require('fs');
const mqtt = require('mqtt');

const client = mqtt.connect('mqtt://broker.hivemq.com');

client.on('connect', () => {
  console.log("Publisher connected to broker");

  const img = fs.readFileSync('test.jpg');

  const base64Image = img.toString('base64');

  client.publish('image/topic', base64Image, { qos: 1 }, () => {
    console.log("Image published as Base64");
    client.end();
  });
});