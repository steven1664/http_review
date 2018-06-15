import datetime
import os

def makereportFolder():
    reporttime = datetime.datetime.now().strftime("_%m_%d_%y_%H_%M_%S")
    directory = os.getcwd() + '/report' + reporttime
    if not os.path.exists(directory):
        os.makedirs(directory)

    return directory
