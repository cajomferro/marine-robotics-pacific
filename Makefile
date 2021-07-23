all: upload

upload:
	rsync -av pacific/ pi@pac:/home/pi/pacific/ --exclude="*.pyc" --exclude="__pycache__"
	rsync -av test_lin_act.py pi@pac:/home/pi/test_lin_act.py
	rsync -av test_icm20948.py pi@pac:/home/pi/test_icm20948.py
	rsync -av libs/ms5837-python/ms5837/ms5837.py pi@pac:/home/pi/pacific/
	rsync -av libs/ms5837-python/example.py pi@pac:/home/pi/test_ms5837.py

ssh:
	ssh pi@pac
