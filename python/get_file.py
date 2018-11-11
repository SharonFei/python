import os
import sys
import time
import datetime

file_dir = 'storage/827C-12ED/Android/media/com.nauto.n2/originalVideo'
list_0 = []  # type: List[Any]
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []



def get_file():
    args = sys.argv[1]
    try:
        os.system('adb shell ls  /storage/827C-12ED/Android/media/com.nauto.n2/originalVideo/20180918 > D:/Node_Installation/home/logs/20180918.txt')
    except Exception as e:
        print(e)


def get_file_2():
    try:
        os.system('adb shell ls  /storage/827C-12ED/Android/media/com.xxx.n2/originalVideo/20180919 > D:/Node_Installation/home/logs/20180919.txt')
    except Exception as e2:
        print(e2)
'''
class AnalysisFile(object):

    def analysis_file(self, path):
        print(path)
        if os.path.exists(path+'/anr'):
            file_list = os.listdir(path+'/anr')
            for i in range(0, len(file_list)):
                file = os.path.join(path+'/anr', file_list[i])
                if os.path.isfile(file):
                    with open(file) as f:
                        print(file)
        #exit(result)
        print(result)
'''


def get_time_stamp():
    with open('D:/20180918.txt') as f:
        for line in f.readlines():
            file_name_list = line.split(' ')[-1].split('.')[0].split('_')
            #print(file_name_list)
            if file_name_list[0] == '0':
                list_0.append(file_name_list[1])
            else:
                list_1.append(file_name_list[1])
    with open('D:/20180919.txt') as f:
        for line in f.readlines():
            file_name_list = line.split(' ')[-1].split('.')[0].split('_')
            #print(file_name_list)
            if file_name_list[0] == '0':
                list_2.append(file_name_list[1])
            else:
                list_3.append(file_name_list[1])


def analysis_time_stamp():
    length = len(list_0)
    print length
    for i in range(0, length):
        time_stamp = (int(list_0[i]) - int(list_0[i-1])) / 1000
        for  i in range(0, length):
            if time_stamp < 300:
                return True
            else:
                break
    length_1 = len(list_1)
    print length_1
    for i in range(0, length_1):
        time_stamp = (int(list_1[i]) - int(list_0[i - 1])) / 1000
        if time_stamp < 300:
            print True
        else:
            break
    length_2 = len(list_2)
    print length_2
    print list_1[-1]
    print list_2[0]
    time_stamp = (int(list_2[0])-int(list_1[-1]))/1000
    time_stamp_2 = (int(list_2[1])-int(list_2[0]))/1000
    if time_stamp < 300:
        print True
    else:
        print False
    if time_stamp_2 < 300:
        print True
    else:
        print False




'''
class FileName(object):
    def get_file(self, file_dir):
        file_list = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.mp4':
                   file_list.append(os.path.join(root, file))
        return file_list

    def list_dir(self, path, file):
        file.write(path+'\n')
        fileNum = 0
        for line in os.listdir(path):
            file_path = os.path.join(path, line)
            if os.path.isdir(file_path):
               myfile.write(''+line+'//'+'\n')
               for li in os.listdir(file_path):
                   myfile.write(''+li+'\n')
                   fileNum = fileNum+1
            elif os.path:
                myfile.write(''+line+'\n')
                fileNum = fileNum + 1
                myfile.write('all the file num is '+str(fileNum))
            myfile.close()
'''
def main():
    '''
    file=AnalyzeFile()
    file.analysis_file('/storage/827C-12ED/Android/media/com.nauto.n2/originalVideo')
    '''
    get_file_2()
    get_time_stamp()
    analysis_time_stamp()
    print (list_0)
    print (list_1)
    get_file()
    print args


if __name__=='__main__':
    main()
    deviceID = None
    benchMarkImg = None
    autoscreenshot = False
    queryImg = None
    outPutImg = None
    rate = 0.98
    duration = None
    moveto = None

    for i in range(0, len(sys.argv)):
        if sys.argv[i] == '-d':
            deviceID = sys.argv[i+1]
        elif sys.argv[i] == '-b':
            benchMarkImg = sys.argv[i+1]
        elif sys.argv[i] == '-q':
            queryImg = sys.argv[i+1]
        elif sys.argv[i] == '-o':
            outPutImg = sys.argv[i+1]
        elif sys.argv[i] == '-r':
            rate = float(sys.argv[i+1])
        elif sys.argv[i] == '-l':
            duration = int(sys.argv[i+1])
        elif sys.argv[i] == '-m':
            coordinates = str(sys.argv[i+1]).split(':')


    print '[INFO] deviceID:', deviceID
    print '[INFO] benchMarkImg:', benchMarkImg
    print '[INFO] queryImg:', queryImg
    print '[INFO] outPutImg:', outPutImg
    print '[INFO] rate:', rate
    print '[INFO] longPress duration:', duration
    print '[INFO] moveto coordinate:', moveto






