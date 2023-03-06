import os 
import shutil
from ctypes import *
import string
import random
import time 

diskLetter = input('|X| Enter disk letter:')

def myFmtCallback(command, modifier, arg):
    print(command)
    return 1

def formatDisk(drive, type, title):
    fm = windll.LoadLibrary('fmifs.dll')
    FMT_CB_FUNC = WINFUNCTYPE(c_int, c_int, c_int, c_void_p)
    FMIFS_UNKNOWN = 0
    fm.FormatEx(c_wchar_p(drive.upper()+':\\'), FMIFS_UNKNOWN, c_wchar_p(type), c_wchar_p(title), True, c_int(0), FMT_CB_FUNC(myFmtCallback))
    print('|X| Done formating the drive')

def createLastFile(DL):
    letter = string.ascii_letters
    numbers = string.digits
    char = string.punctuation
    res = ''.join(random.choice(letter+numbers+char) for i in range(47185920))
    f = open(DL.upper()+':\/'+'lastfile.txt','w')
    f.write(res)
    f.close()
    

def createFile(DL):
    letters = string.ascii_letters
    numbers = string.digits
    char = string.punctuation
    resTextInside = ''.join(random.choice(letters + numbers + char) for i in range(524288000)) # 1073741824
    f = open(DL.upper()+':\/'+ 'fillfile.txt', 'w')
    f.write(resTextInside)
    f.close()
    print('|X| Done Creating file ')
   
def copyFileMade(DL,size):
    letter = string.ascii_letters
    res = ''.join(random.choice(letter)for i in range(8))
    print('|X| This will take a while so be patient ,waiting to finish copying ')
    for x in range(size * 2 + 2):
        shutil.copy2(DL.upper()+':\/fillfile.txt', os.path.join(DL.upper()+':\/fillfile{}.txt').format(x))
        time.sleep(5)      
    
try:
    total, used, free = shutil.disk_usage(diskLetter.upper() + ':\/')
    print("|X| Total: %d GiB" % (total // (2**30)))
    print("|X| Used: %d GiB" % (used // (2**30)))
    print("|X| Free: %d GiB" % (free // (2**30)))
    print("\033[1;31;40m|X||X|IMPORTANT NOTE : If you continue with this script this ,")
    print("\033[1;31;40m|X||X|will remove everything from the drive")
    lastCheckPoint = input('\033[1;37;40m|X| Do you want to continue? (y/n): ')
    if lastCheckPoint == 'y':
        nTotal = (total // (2**30))
        print('|X| Formating disk ')
        formatDisk(diskLetter,'NTFS','CleanerDrive')
        print('|X| Creating fillFile please wait it might take some time .')
        createFile(diskLetter)
        copyFileMade(diskLetter,nTotal)
        createLastFile(diskLetter)
        formatDisk(diskLetter,'NTFS','CleanerDrive')
        print('|X| Done !!!')
        exit
    else:
        exit
except Exception as e:
    print('\033[1;31;40m |X|Invalid Disk Letter or the disk is not available \n')
    print(e)
    