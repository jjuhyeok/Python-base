t = int(input())

hour = t/3600
min = (t % 3600) / 60
sec = (t % 3600) % 60
print("%d시간 %d분 %d초"%(hour,min,sec))
