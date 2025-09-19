const mqtt = require('mqtt');

//const client = mqtt.connect('mqtt://127.0.0.1:1883');
const client = mqtt.connect('mqtt://broker.hivemq.com');

let receive_data = [];

const PUBLISHER_TYPE = "json"; // txt, json
const TOPIC = 'openhouse/qrscan';

function connectBroker() {
  client.on('connect', () => {
    console.log("qrscan subscriber connect to broker");
    subscribeTopic(TOPIC);
  });
}

function subscribeTopic(topic) {
  client.subscribe(topic, (err) => {
    if (!err) {
      console.log(`waiting topic : ${topic} ...`);
    } else {
      console.error(`failed to subscribe topic : ${topic}`, err);
    }
  });

  client.on('message', handleMessage);
}

function handleMessage(topic, message) {
  try {
    const msg_string = message.toString();
    let data_array = [];

    const parsed = JSON.parse(msg_string);

    if (PUBLISHER_TYPE === "json") {
      data_array = Array.isArray(parsed) ? parsed : [parsed];
    } else if (PUBLISHER_TYPE === "txt") {
      data_array = [parsed];
    }

    data_array.forEach(data => {
      if (data.epoch) {
        const date = new Date(data.epoch * 1000);
        const thai_time = date.toLocaleString('th-TH', {timeZone: 'Asia/Bangkok'});
        data.thai_time = thai_time;
      }
      receive_data.push(data);
      console.log("receive : ", data);
    });

  } catch (e) {
    console.error("error parsing message : ", message.toString());
  }
}

connectBroker();