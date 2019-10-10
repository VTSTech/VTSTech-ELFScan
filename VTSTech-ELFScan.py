import sys, pycdlib

def banner():
	print("##########################################");
	print("# VTSTech-ELFScan v0.0.2                 #");
	print("# Facebook: fb.me/VTSTech                #");
	print("# Twitter: @VTSTech_                     #");
	print("# Web: www.VTS-Tech.org                  #");
	print("# E-mail: veritas@vts-tech.org           #");
	print("# BTC 1ByfBujg9bnmk1XXY2rxY6obhqHMUNiDuP #");
	print("##########################################\n");
           	
if len(sys.argv) == 1:
	banner()
	print('Usage: VTSTech-ELFScan.py -irx "C:\ISO\Backup File.iso"\n\nOptions:\n\n-irx Filter .IRX results\n');
	sys.exit()
print("##########################")
print("# VTSTech-ELFScan v0.0.2 #")
print("##########################\n\n")
iso = pycdlib.PyCdlib()
if (sys.argv[1] == "-irx"):
	noirx=int(1)
	iso.open(sys.argv[2])
else:	
	noirx=int(0)
	iso.open(sys.argv[1])

for dirname, dirlist, filelist in iso.walk(iso_path='/'):
	for target in filelist:
		if (len(dirname) == 0):
			fn = target
		else:
			fn = dirname+"/"+target
		with iso.open_file_from_iso(iso_path=str(fn)) as infp:
			first = infp.read(24)
			if ((first[1:4]==b'ELF') and (noirx==int(0))):
				print("ELF Detected!:"+fn.replace("//","/"))
			elif (((first[1:4]==b'ELF') and (noirx==int(1)) and (fn[-5:-2] != "IRX"))):
				print("ELF Detected!:"+fn.replace("//","/"))
iso.close()