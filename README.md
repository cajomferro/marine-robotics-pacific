# marine-robotics-pacific

## Upload and connect
```
make upload
make ssh
```

## Available scripts

```
python test_pitch.py --open
python test_pitch.py --close
python test_pitch.py --set 70

python test_syringe.py --open
python test_syringe.py --close
python test_syringe.py --set 70

python test_icm20948.py

python test_ms5837.py

```

Qwiic available sensors:

```
$: import qwiic
$:qwiic.list_devices()
$:[
(16, 'Qwiic Button', 'QwiicButton'), 
(16, 'Qwiic Titan GPS', 'QwiicTitanGps'), 
(16, 'Qwiic 4m Distance Sensor (ToF)', 'QwiicVL53L1X'), 
(16, 'Qwiic PIR', 'QwiicPIR'), 
(64, 'Qwiic PCA9685', 'QwiicPCA9685'), 
(64, 'Qwiic Button', 'QwiicButton'), 
(64, 'Qwiic 4m Distance Sensor (ToF)', 'QwiicVL53L1X'), 
(64, 'Qwiic PIR', 'QwiicPIR'), 
(64, 'Pi Servo HAT', 'PiServoHat'), 
(105, 'Qwiic PCA9685', 'QwiicPCA9685'), 
(105, 'Qwiic ICM20948', 'QwiicIcm20948'), 
(105, 'Qwiic Button', 'QwiicButton'), 
(105, 'Qwiic 4m Distance Sensor (ToF)', 'QwiicVL53L1X'), 
(105, 'Qwiic PIR', 'QwiicPIR'), 
(112, 'Qwiic PCA9685', 'QwiicPCA9685'), 
(112, 'Qwiic Button', 'QwiicButton'), 
(112, 'Qwiic 4m Distance Sensor (ToF)', 'QwiicVL53L1X'), 
(112, 'Qwiic PIR', 'QwiicPIR'), 
(112, 'Qwiic Mux', 'QwiicTCA9548A')
]
```

