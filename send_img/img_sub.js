const fs = require('fs');
const mqtt = require('mqtt');

const client = mqtt.connect('mqtt://broker.hivemq.com');

client.on('connect', () => {
  console.log("Subscriber connected to broker");

  client.subscribe('image/topic', (err) => {
    if (!err) {
      console.log("waiting topic : image/topic ...");
    }
  });
});

client.on('message', (topic, message) => {
  console.log("Image received from : ", topic);

  const buffer = Buffer.from(message.toString(), 'base64');

  fs.writeFileSync('received.jpg', buffer);
  console.log("Image saved as received.jpg");
});