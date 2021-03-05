#Download datasets from NCBI URL in parts

import urllib
import wget
from xml.etree.ElementTree import parse

#For bacterial proteins in refseq database
var_url = urllib.request.urlopen('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=protein&term=bacteria[Organism]+AND+srcdb_refseq[prop]&usehistory=y')
xmldoc = parse(var_url)

#Get the Web environment ID to download 
webenv = xmldoc.findtext("WebEnv")
print(webenv)
#Fetch the first 500 results
dfrom = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&WebEnv="+webenv+"&query_key=1&retstart=0&retmax=500&rettype=fasta&retmode=text"

wget.download(dfrom)

#Fetch consecutive 500 results until (~/< 1000) all are downloaded

for pos in [0,500]:
    dfrom = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=protein&WebEnv="+webenv+"&query_key=1&retstart="+str(pos)+"&retmax=500&rettype=fasta&retmode=text"
    wget.download(dfrom)
