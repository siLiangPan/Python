# -*- coding: UTF-8 -*-
import os

path=None
if path is None:  
    if os.name == 'nt':  
        path = "C:\\"  
    else:  
        path = '/'  
if os.name == 'nt':  
    import win32file  
    res_list = win32file.GetDiskFreeSpace(path)  
    disk_free_space = str(res_list[0]*res_list[1]*res_list[2]/(1024*1024*1024.0))+"G"  
else:  
    import statvfs  
    vfs = os.statvfs(path)  
    disk_free_space = vfs[statvfs.F_BAVAIL]*vfs[statvfs.F_BSIZE]/(1024*1024.0)  
    
print(disk_free_space)