# MQTT System for Mini-Project (Software Development Practice I)

This project implements a **communication protocol using MQTT** for the course **010123131 Software Development Practice I (2025-1) Mini-Project**.  

The project is divided into **two main parts**:

---

## Project Structure
mqtt_system/
- qrscan/
   - qrscan_sub.js (subscribe : receive data via MQTT)
   - qrscan_pub.js (publish : read qrscan_data file and send data via MQTT)
   - qrscan_data.json
   - qrscan_data.txt (optional)
   - gen_data.py (generate example data)
- register/
   - register_sub.js (subscribe : receive data via MQTT)
   - register_pub.js (publish : read register_data file and send data via MQTT)
   - register_data.json
   - register_data.txt (optional)
   - gen_data.py (generate example data)

---

## How to Run this Project in Window

### Requirements

to run this project, make sure the following are install

1. python (use to run `gen_data.py`)
verify installation
```bash
python --version
```
2. node.js (use to run *_sub.js and *_pub.js for MQTT communication)
verify installation
```bash
node -v
npm -v
```
3. mqtt library (if you are using the file directly and want to create a new project)
```bash
cd 'your script folder'
npm init -y
npm install mqtt
```

### 1) QR Scan (`qrscan` folder)

1. Open Terminal/Command Prompt and go to `qrscan` folder
```bash
cd mqtt_system/qrscan
```
2. Generate example data (if you need to test)
```bash
python gen_data.py
```
3. Run the MQTT subscriber (Make sure that PUBLISHER_TYPE in qrscan_sub.js is set to JSON)
```bash
node qrscan_sub.js
```
4. Run the MQTT publisher (Make sure that PUBLISHER_TYPE in qrscan_sub.js is set to JSON and qrscan_data.json file is in the same folder)
```bash
node qrscan_pub.js
```

### 2) Register (`register` folder)

1. Open Terminal/Command Prompt and go to `register` folder
```bash
cd mqtt_system/register
```
2. Generate example data (if you need to test)
```bash
python gen_data.py
```
3. Run the MQTT subscriber (Make sure that PUBLISHER_TYPE in register_sub.js is set to JSON)
```bash
node register_sub.js
```
4. Run the MQTT publisher (Make sure that PUBLISHER_TYPE in register_sub.js is set to JSON and register_data.json file is in the same folder)
```bash
node register_pub.js
```



