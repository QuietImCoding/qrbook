import pyqrcode
import sys
import os, glob
from multiprocessing import Pool
from time import sleep
from progress.bar import Bar

fname = sys.argv[1]
fsize = os.path.getsize(fname)
chunksize = 800
chunksneeded = fsize // chunksize 
chunk = "owo"

print("Getting QR codes for data in " +
      str(chunksize) + "byte blocks")
print("File: " + fname +", " + str(fsize) + "B")
print(str(chunksneeded) + " chunks needed")
sleep(3)
chunklist = []
filemap = []

with open(fname, 'rb') as myfile:
    with Bar('Mapping File', max=chunksneeded+1) as bar:
        while chunk != b'':
            chunk = myfile.read(chunksize)
            #print(str(chunk))
            if chunk == b'':
                break
            filemap.append(chunk)
            bar.next()
            

def mkchunk(dat):
    try:
        return [pyqrcode.create(dat, mode='binary', encoding='cp437', error='L')]
    except Exception as e:
        return [ pyqrcode.create(data, mode='binary', encoding='cp437', error='L') for data in (dat[0:len(dat)//2], dat[len(dat)//2:]) ]

chunknum = 0    
print("Generating chunks")
with Pool(20) as p:
    chunklist = p.map(mkchunk, filemap)


print("Normalizing chunk list")
chunklist = [item for sublist in chunklist for item in sublist]

print("Cleaning up old codes")
files = glob.glob('qrcodes/*')
for f in files:
    os.remove(f)
    
chunknum = 0
print("Writing qr codes")
for qcode in chunklist:
    qcode.png('qrcodes/qrcode_' + str(chunknum) + ".png")
    print("Wrote chunk " + str(chunknum) + " of " + str(chunksneeded))
    chunknum += 1

print("Combining into gif...")
os.system('convert -interpolate Nearest -filter point -delay 1 "qrcodes/*[500x]" animqr.gif')
