const mqtt = require('mqtt');

//const client = mqtt.connect('mqtt://127.0.0.1:1883');
const client = mqtt.connect('mqtt://broker.hivemq.com');

let receive_data = [];

const PUBLISHER_TYPE = "json"; // txt, json
const TOPIC = 'openhouse/register';

function connectBroker() {
  client.on('connect', () => {
    console.log("register subscriber connected to broker");
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
      receive_data.push(data);

      console.log("received : ");
      console.table([{
        FirstName: data.firstName,
        LastName: data.lastName,
        Age: data.age,
        Gender: data.gender,
        School: data.school,
        Email: data.email,
        Phone: data.phone
      }]);
    });

  } catch (e) {
    console.error("error parsing message : ", message.toString());
  }
}

connectBroker();