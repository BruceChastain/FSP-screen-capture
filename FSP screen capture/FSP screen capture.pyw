import datetime
import sys
import os
import shutil
from PyQt4.QtGui import QPixmap, QApplication

# ---- Grab the screen shot
app = QApplication(sys.argv)
now = datetime.datetime.now()
date_and_time = now.strftime("%Y_%m_%d_%H_%M_%S")
QPixmap.grabWindow(QApplication.desktop().winId()).save(date_and_time, 'png')

# ---- Create he screencaps folder if needed and copy the captures to the folder
folder = "screencaps"
src = date_and_time

if not os.path.exists(folder):
    os.mkdir( folder, 0755 );
   
if os.path.exists(folder):
    shutil.move(src, folder)





    
