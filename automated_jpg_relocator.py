from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os 
import time 

# if downloaded file has 'jpg' extension, move to new dir on desktop
class myHandler(FileSystemEventHandler): 

    def on_modified(self, event):
        for filename in os.listdir(tracked_folder):
            if filename and filename.endswith("jpg"): 
                src =  tracked_folder + "/" + filename
                new_destination = folder_destination + "/" + filename 
                os.rename(src, new_destination)

tracked_folder = "/Users/dermot/downloads"
folder_destination = "/Users/dermot/desktop/newFolder"


#Observe for event, recursive nature searches sub-directories
event_handler = myHandler()
observer = Observer()
observer.schedule(event_handler, tracked_folder, recursive=True)
observer.start()

try: 
    while True: 
        time.sleep(7)
except KeyboardInterrupt: 
    observer.stop()
observer.join()