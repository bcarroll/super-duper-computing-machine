
from re import sub
from types import FunctionType
import psutil

class MemoryStats():
	def __init__(self):
		"""
		statKeys contains a list the available memory statistics (memInfoKey)
		"""
		self.statKeys = []
		self.getStats()

	def getStats(self, memInfoKey=None):
		"""
		parameters: 
			memInfoKey <str> an element from the statKeys list
		returns:
			<dict> containing the value and format for the specified memInfoKey
		"""
		_meminfo = open('/proc/meminfo').read()

		# Strip tabs
		_meminfo = _meminfo.replace("\t","")

		# Turn into list at return
		_meminfo = _meminfo.split("\n")

		# Filter empty strings
		_meminfo = filter(len, _meminfo)
		
		allMemInfo = {}
		# Split into key/value dict
		for item in _meminfo:
			key,val = item.split(':')
			key = key.replace('(','_').replace(')','')
			val = sub("^\s+", "", val)
			val,format = val.split(' ')
			if key == memInfoKey:
				return {"value": val, "format": format}
			else:
				# This is intended to only be executed once
				# ... when the class instance is initialied
				if key not in self.statKeys:
					self.statKeys.append(key)
		
if __name__ == '__main__':
	meminfo = MemoryStats()
	print(dir(meminfo))
	for key in meminfo.statKeys:
		print('%s : %s' % (key, meminfo.getStats(key)['value']))

#memTotal     = sub("^\s_meminfo['MemTotal'].replace(/^\s+//,'')#        1933244 kB
#memFree      = _meminfo['MemFree']#          577264 kB
#memAvailable = _meminfo['MemAvailable']#    1304536 kB
#buffers      = _meminfo['Buffers']#          106812 kB
#cached       = _meminfo['Cached']#           774744 kB
#swapCached   = _meminfo['SwapCached']#            0 kB
#active       = _meminfo['Active']#           820776 kB
#inactive     = _meminfo['Inactive']#         396472 kB
#activeAnon   = _meminfo['Active(anon)']#     336368 kB
#inactiveAnon = _meminfo['Inactive(anon)']#   107140 kB
#activeFile   = _meminfo['Active(file)']#     484408 kB
#inactiveFile = _meminfo['Inactive(file)']#   289332 kB
#unevictable  = _meminfo['Unevictable']#          16 kB
#mLocked      = _meminfo['Mlocked']#              16 kB
#highTotal    = _meminfo['HighTotal']#       1179648 kB
#highFree     = _meminfo['HighFree']#         142140 kB
#lowTotal     = _meminfo['LowTotal']#         753596 kB
#lowFree      = _meminfo['LowFree']#          435124 kB
#swapTotal    = _meminfo['SwapTotal']#        102396 kB
#swapFree     = _meminfo['SwapFree']#         102396 kB
#dirty        = _meminfo['Dirty']#                96 kB
#writeback    = _meminfo['Writeback']#             0 kB
#anonPages    = _meminfo['AnonPages']#        335736 kB
#mapped       = _meminfo['Mapped']#           209324 kB
#shmem        = _meminfo['Shmem']#            107820 kB
#slab         = _meminfo['Slab']#              88916 kB
#sreclaimable = _meminfo['SReclaimable']#      46796 kB
#sunreclaim   = _meminfo['SUnreclaim']#        42120 kB
#kernelStack  = _meminfo['KernelStack']#        2576 kB
#pageTables   = _meminfo['PageTables']#         9356 kB
#nfsUnstable  = _meminfo['NFS_Unstable']#          0 kB
#bounce       = _meminfo['Bounce']#                0 kB
#writebackTmp = _meminfo['WritebackTmp']#          0 kB
#commitLimit  = _meminfo['CommitLimit']#     1069016 kB
#committedAS  = _meminfo['Committed_AS']#    2331520 kB
#vmallocTotal = _meminfo['VmallocTotal']#     245760 kB
#vmallocUsed  = _meminfo['VmallocUsed']#           0 kB
#vmallocChunk = _meminfo['VmallocChunk']#          0 kB
#perCpu       = _meminfo['Percpu']#              752 kB
#cmaTotal     = _meminfo['CmaTotal']#         262144 kB
#cmaFree      = _meminfo['CmaFree']#          237180 kB