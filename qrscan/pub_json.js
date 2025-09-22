const fs = require('fs');
const mqtt = require('mqtt');

const client = mqtt.connect('mqtt://broker.hivemq.com');

client.on('connect', () => {
  console.log("JSON Publisher connected to broker");

  const raw_data = fs.readFileSync('qrscan_data.json', 'utf8');
  const data = JSON.parse(raw_data);

  data.forEach((message, index) => {
    client.publish('openhouse/qrscan', JSON.stringify(message));
    console.log(`send message #${index + 1}:`, message);
  });

  client.end();
});