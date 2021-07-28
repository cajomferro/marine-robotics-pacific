HOST=raspberrypi.local
#RSYNC_OPTS=-r --size-only --no-times
RSYNC_OPTS=-a

all: upload

upload:
	rsync $(RSYNC_OPTS) --delete pacific/ pi@$(HOST):/home/pi/pacific/ --exclude="*.pyc" --exclude="__pycache__"
	rsync $(RSYNC_OPTS) test_syringe.py pi@$(HOST):/home/pi/test_syringe.py
	rsync $(RSYNC_OPTS) test_imu.py pi@$(HOST):/home/pi/test_imu.py
	rsync $(RSYNC_OPTS) test_pitch.py pi@$(HOST):/home/pi/test_pitch.py
	rsync $(RSYNC_OPTS) test_roll.py pi@$(HOST):/home/pi/test_roll.py
	rsync $(RSYNC_OPTS) test_godown.py pi@$(HOST):/home/pi/test_godown.py
	rsync $(RSYNC_OPTS) libs/ms5837-python/ms5837/ms5837.py pi@$(HOST):/home/pi/pacific/
	rsync $(RSYNC_OPTS) libs/ms5837-python/example.py pi@$(HOST):/home/pi/test_ms5837.py

ssh:
	ssh pi@$(HOST)
