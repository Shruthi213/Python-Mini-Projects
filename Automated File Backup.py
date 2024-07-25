import os
import shutil
import datetime
import schedule
import time

source_dir = ""
destination_dir = ""

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copy to : {dest_dir}")
    except FileExistsError:
        print(f"Folder already exist in : {dest}")

schedule.every().day.at("6:55").do(Lambda: copy_folder_to_directory(source_dir, destination_dir))


while True:
    schedule.run_pending()
    time.sleep(60)