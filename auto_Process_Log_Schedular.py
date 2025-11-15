import psutil       # type: Error
import time
import os
import schedule
######################################################################################
# Function: Scan running processes
#  Author: Nikita Omase
# Date : 15/11/2025
#####################################################################################
def ProcessScan():
    listprocess = []
    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=['pid', 'name', 'username'])
            info['vms'] = proc.memory_info().vms / (1024 * 1024)  # memory usage in MB
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print("Exception occurred")
    return listprocess
###################################################################################################
# Function: Create log file with process info
#  Author: Nikita Omase
# Date : 15/11/2025
#####################################################################################
def CreateLog(FolderName):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.ctime().replace(" ", "").replace(":", "_").replace("/", "_")
    filename = os.path.join(FolderName, f"Marvellous{timestamp}.log")

    with open(filename, 'w') as fobj:
        border = "-" * 80
        fobj.write(border + "\n")
        fobj.write("\t\tMarvellous Infosystem Process Log\n")
        fobj.write(f"\t\tLog file created at: {time.ctime()}\n")
        fobj.write(border + "\n\n")

        data = ProcessScan()
        for value in data:
            fobj.write(f"{value} \n\n")

        fobj.write(border)
##################################################################################################
# Function: Schedule logging every 6 minutes
# Author: Nikita Omase
# Date : 15/11/2025
##################################################################################################
def main():
    schedule.every(6).minutes.do(CreateLog, "MarvelllousProcessX")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()