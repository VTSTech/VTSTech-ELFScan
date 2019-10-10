import sys, pycdlib

def banner():
	print("##########################################");
	print("# VTSTech-ELFScan v0.0.1                 #");
	print("# Facebook: fb.me/VTSTech                #");
	print("# Twitter: @VTSTech_                     #");
	print("# Web: www.VTS-Tech.org                  #");
	print("# E-mail: veritas@vts-tech.org           #");
	print("# BTC 1ByfBujg9bnmk1XXY2rxY6obhqHMUNiDuP #");
	print("##########################################\n");
	print('Usage: VTSTech-ELFScan.py "C:\ISO\Backup File.iso"\n');
           	
if len(sys.argv) == 1:
	banner()
	sys.exit()
banner()	
iso = pycdlib.PyCdlib()
iso.open(sys.argv[1])

for dirname, dirlist, filelist in iso.walk(iso_path='/'):
	for target in filelist:
		if (len(dirname) == 0):
			fn = target
		else:
			fn = dirname+"/"+target
		with iso.open_file_from_iso(iso_path=str(fn)) as infp:
			first = infp.read(24)
			if (first[1:4]==b'ELF'):
				print("ELF Detected!:"+fn.replace("//","/"))
iso.close()