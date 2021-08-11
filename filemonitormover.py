from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

folder_to_track = "exampledir"
folder_destination = "endingdir"

class Myhandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)



event_handler = Myhandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()