const fs = require('fs');
const mqtt = require('mqtt');

//const client = mqtt.connect('mqtt://127.0.0.1:1883');
const client = mqtt.connect('mqtt://broker.hivemq.com');

client.on('connect', () => {
  console.log("Publisher connected to broker");

  const lines = fs.readFileSync('qrscan_data.txt', 'utf8').split('\n').filter(Boolean);

  lines.forEach((line, index) => {
    const [token, location, check, epoch] = line.split(',');
    const message = {
      token,
      location,
      check: Number(check),
      epoch: Number(epoch)
    };

    client.publish('openhouse/qrscan', JSON.stringify(message));
    console.log(`send message #${index + 1}:`, message);
  });

  client.end();
});