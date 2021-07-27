HOST=pac.wifi

all: upload

upload:
	rsync -av pacific/ pi@$(HOST):/home/pi/pacific/ --exclude="*.pyc" --exclude="__pycache__"
	rsync -av test_syringe.py pi@$(HOST):/home/pi/test_syringe.py
	rsync -av test_imu.py pi@$(HOST):/home/pi/test_imu.py
	rsync -av test_pitch.py pi@$(HOST):/home/pi/test_pitch.py
	rsync -av test_roll.py pi@$(HOST):/home/pi/test_roll.py
	rsync -av libs/ms5837-python/ms5837/ms5837.py pi@$(HOST):/home/pi/pacific/
	rsync -av libs/ms5837-python/example.py pi@$(HOST):/home/pi/test_ms5837.py

ssh:
	ssh pi@$(HOST)
