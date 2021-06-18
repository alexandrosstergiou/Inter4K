import os
import glob
from multiprocessing import Pool

resolutions = {'QHD':[2560,1440],
               'FHD':[1920,1080],
               'HD':[1280,720],
               'qHD':[960,540],
               'nHD':[640,360]
}

frame_rates = [50,30,24,15]


def res(tmp):
    filename = tmp[0]
    res = tmp[1]
    width = tmp[2]
    height = tmp[3]
    if not os.path.isdir('Inter4K/60fps/{}'.format(res)):
        os.makedirs('Inter4K/60fps/{}'.format(res))
    if os.path.isfile('Inter4K/60fps/{0}/{1}'.format(res,filename)):
        return
    os.system('ffmpeg -i 60fps/UHD/{0} -vf scale={1}:{2} Inter4K/60fps/{3}/{0}'.format(filename, width,height,res))

def f_rate(tmp):
    file = tmp[0]
    fps = tmp[1]
    _, res, filename = file.split('/')
    if not os.path.isdir('Inter4K/{0}fps/{1}'.format(fps,res)):
        os.makedirs('Inter4K/{0}fps/{1}'.format(fps,res))
    if os.path.isfile('Inter4K/{0}fps/{1}/{2}'.format(fps,res,filename)):
        return
    os.system('ffmpeg -i {0} -filter:v fps={1} Inter4K/{1}fps/{2}/{3}'.format(file,fps,res,filename))

# Resolution
for file in glob.glob('Inter4K/60fps/UHD/*.mp4'):
    filename = file.split('/')[-1]

    targets = [ [filename,key,resolutions[key][0],resolutions[key][1]] for key in resolutions.keys() ]

    with Pool(16) as p:
        print(p.map(res, targets))

# FPS
for file in glob.glob('Inter4K/60fps/*/*.mp4'):
    targets = [ [file,fps] for fps in frame_rates  ]

    with Pool(16) as p:
        print(p.map(f_rate, targets))
