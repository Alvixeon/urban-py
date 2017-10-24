#imports
import requests,lxml
from lxml import html
#end imports

#globals
global trm
global finalurl
#end globals

def define(trm):
	trm = parseTerm(trm)
	finalurl = "https://www.urbandictionary.com/define.php?term=" + trm
	pageContent=requests.get(finalurl)
	tree = html.fromstring(pageContent.content)
	final = tree.xpath('//*[@id="content"]/div[1]/div[3]//text()')
	
	if "Define it!" in final:
		return "[*] This term does not appear to exist on the urbandictionary site, please try a different string"
	else:
		finstr = ''.join(final)
		#print (trm + " - " + finstr) debug testing
		return finstr

def example (ex):
	ex = parseTerm(ex)
	finalurl = "https://www.urbandictionary.com/define.php?term=" + ex
	pageContent=requests.get(finalurl)
	tree = html.fromstring(pageContent.content)
	final = tree.xpath('//*[@id="content"]/div[1]/div[4]//text()')
		
	if "Define it!" in final:
		return "[*] This term does not appear to exist on the urbandictionary site, please try a different string"
	else:
		finstr = ''.join(final)
		#print ("Ex: " + finstr) debug testing
		return finstr
	
	
def parseTerm(trm):
	trm = trm.replace(" " , "+")
	return trm


#if __name__ == "__main__": #moreeee debug testing
	#define("cow")
	#example("cow")
