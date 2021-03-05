from ftplib import FTP
import os
import wget 


os.mkdir("wormbase")
os.chdir("wormbase")
os.mkdir("genomic")
os.mkdir("transcriptomic")
os.mkdir("proteomic")
os.mkdir("annotations")

#Parent URL
url = "ftp.wormbase.org/pub/wormbase/releases/current-development-release/species/"

#Split URL into two halves
host,file_path = url.split('/', 1)

#Login to parent URL server
ftp = FTP(host)
ftp.login()

#Change directory here
ftp.cwd(file_path)

#Verify directory
ftp.pwd()

#Only keep names of strains
content = ftp.nlst()
strains = list(filter(lambda x: 'json' not in x,content))

#ROUGH: if annotation folder exists, download those extra files
flag = 1
try:
    for s in strains:
        flag = flag + 1

        #Enter this strain's directory
        ftp.cwd(s+'/')
        print('\n'+ftp.pwd())

        #Enter this project's directory
        for internal in ftp.nlst():
            print("\t"+internal)
            ftp.cwd(internal)
            
            t = ftp.nlst()
            #print(t)
            
            if "annotation" == t[0]:
                location = "annotation"
                print("AHA")
                ftp.cwd(location)
                rex = ftp.nlst()
                required_terms = ["functional_description","protein_domain","go_annotation"]
                for r in rex:
                    if any(term in r for term in required_terms):
                        print("Down this: ", r)
                        wget.download('ftp://ftp.wormbase.org'+ftp.pwd()+'/'+r,"annotations",bar=False)
                        
        if flag == 2:
            break
except:
    print("OOF")
    ftp.cwd("../..")
