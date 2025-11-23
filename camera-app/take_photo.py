from picamera2 import Picamera2
from datetime import datetime
import os
import shutil
import time

# Save into Next.js public folder:
output_dir = "/home/jehau/GIT/vilde/vildesdisciple/public/photos"
os.makedirs(output_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"{output_dir}/{timestamp}.jpg"
latest_filename = f"{output_dir}/latest.jpg"

picam2 = Picamera2()
config = picam2.create_still_configuration({"size": (1920, 1080)})
picam2.configure(config)

picam2.start()
time.sleep(1)
picam2.capture_file(filename)
picam2.stop()

# Update latest feed image
shutil.copyfile(filename, latest_filename)

print(f"Saved: {filename}")
print("Updated latest.jpg")
