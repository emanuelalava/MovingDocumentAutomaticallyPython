
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import os
import time

class MyHandler(FileSystemEventHandler):
    def on_any_event(self,event):
        for filename in os.listdir(folder_to_track):
            if filename.split(".")[-1]!="crdownload":
                print(filename)


                src = folder_to_track + "/" +filename
                new_destination = folder_destination +"/" +filename
                os.rename(src, new_destination)


folder_to_track = 'C:/Users/emanu/Documents/carpetaOrdenadora'
folder_destination = 'C:/Users/emanu/Downloads/move'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
