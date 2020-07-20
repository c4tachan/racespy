import datetime
import keyboard

from gpiozero import LED
from picamera import PiCamera

class cam:
    camera = PiCamera()
    i = 1
    active = False
    led = LED(16)

def TakePhoto(cmr):
    if not (cmr.active):
        cmr.active = True

        # record the current time stamp
        tm = datetime.datetime.now()

        # Turn off the blue LED
        cam.led.off()

        print(f"Triggered at: {tm}")

        cmr.camera.exif_tags['EXIF.SubSecTime'] = f"{tm}"

        cmr.camera.capture(f"/home/pi/RaceSpyPhotos/testclick-{cmr.i}.jpg")
        
        cmr.i += 1
        print(f"Photo taken at {datetime.datetime.now()}!")

        # Turn On the blue led
        cam.led.on()

        cmr.active = False

def main():
    cmr = cam()
    cmr.active = False
    cmr.camera.resolution = (3280, 2464)
    cmr.camera.shutter_speed = 200
    cmr.led.on()

    pwrLed = LED(14)
    pwrLed.on()

    keyboard.on_release_key('home', lambda _: TakePhoto(cmr))

    input("Press enter to quit.")
        


if __name__ == "__main__":
    main()