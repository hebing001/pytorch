import psutil

# 获取磁盘使用率(windows),linux服务器可以获取根目录/下的磁盘使用率 disk_usage_C = psutil.disk_usage('/')
#disk_usage()方法可以获取指定路径的磁盘使用情况，返回一个namedtuple对象，包含total、used、free、percent四个属性，分别表示总容量、已用容量、可用容量和使用率。

disk_usage_C = psutil.disk_usage('C:')
print("C磁盘总体情况: ","总容量:",round(disk_usage_C.total/1073741824,2),"G"," 磁盘使用率:",disk_usage_C.percent, "%",sep='')
# sep='' 去除print()内空格,round(数值,2)：保留两位小数 ,1G等于1,073,741,824byte

disk_usage_D = psutil.disk_usage('D:')
print("D磁盘使用率：","总容量:",round(disk_usage_D.total/1073741824,2),"G"," 磁盘使用率:",disk_usage_D.percent, "%",sep='')

disk_usage_E = psutil.disk_usage('E:')
print("E磁盘使用率：","总容量:",round(disk_usage_E.total/1099511627776,1),"T"," 磁盘使用率:",disk_usage_E.percent, "%",sep='')

# 获取内存使用率
#virtual_memory()方法可以获取系统内存使用情况，返回一个namedtuple对象，包含total、available、percent、used、free五个属性，分别表示总内存、可用内存、使用率、已用内存和可用内存。
mem = psutil.virtual_memory()
print("内存总量: ",round(mem.total/1073741824,2),"内存使用率：", mem.percent, "%")

# 获取CPU使用率
#cpu_percent()方法可以获取CPU使用率，可以指定采样间隔（默认为1秒），返回一个浮点数，表示CPU使用率
cpu_percent = psutil.cpu_percent(interval=100)
print("cpu核数: ",psutil.cpu_count(),"CPU使用率：", cpu_percent, "%")