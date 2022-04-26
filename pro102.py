
import dropbox
import cv2
import time
import random

startTime=time.time()

def takeSnapshot():
    number = random.randint(1,100)
    videoCaptureObject = cv2.videoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imgname = "img"+str(number)+".png"
        cv2.imwrite(imgname,frame)
        startTime=time.time()
        result = False
    return imgname
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


takeSnapshot()
    
def uploadFile():
    access_token = "sl.BGbeY6cSshcfIXDIFKoOIsRB9rQiIAKcqfxfh8ryOyj-oa1AdTBrJXQT3Ar0cu1ma63__6dPg_NqnugYgdm2iwYH1EbCZlNsf4cOHwNTL52Q41bHt6ityWKslBWFoASj3OfptKE"
    file=imgname
    file_from = file
    file_to = "/pro102" + imgname
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f :
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overWrite)
        print("File has been uploaded.")

def main():
    while(True):
        if((time.time()-startTime)>=3):
            name = takeSnapshot()
            uploadFile()

main()