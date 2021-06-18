import os
import glob

avg_fps = 0
avg_duration = 0
errors = []

for i,file in enumerate(glob.glob('Inter4K/60fps/*/*.mp4')):
  fps = os.popen('ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=r_frame_rate %s'%(file)).read()
  res = os.popen('ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 %s'%(file)).read()
  fps = float(fps.rstrip().split('/')[0]) / float(fps.rstrip().split('/')[1])
  duration = float(os.popen('ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 %s'%(file)).read().rstrip())
  print('{:s} res: {:s} fps: {:.2f} duration:{:.2f}'.format(file,res.rstrip(),fps,duration))
  avg_fps += fps
  avg_duration += duration
  if (avg_fps < 59 or duration < 4.9 or duration > 5.1):
      errors.append('ERROR: {:s} res: {:s} fps: {:.2f} duration:{:.2f}'.format(file,res.rstrip(),fps,duration))

print('avg fps: {:.2f}'.format(avg_fps/i),'avg duration: {:.2f}'.format(avg_duration/i))
for er in errors:
    print(er)
