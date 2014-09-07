"""
-------------------------------------------------------------------------------
Copyright 2014

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-------------------------------------------------------------------------------

http://www.malwerewolf.com/

Author: Destruct_Icon, 8bits0fbr@in, nanoSpl0it, Otakun
Version: 1.0

"""
import subprocess
import os
import sys
import urllib
import urllib2
import time
def main():
	print 'Welcome to your Foremost ALL in ONE\n'
	foremost()
	md5()
	vt()
# Foremost Section
def foremost():
	inputFile = raw_input('Please select the location of your file: ')
	if os.path.isfile(inputFile):
		print 'You have selected ' + inputFile
	else:
		print 'Please give a proper file location.'
		foremost()
	subprocess.call(['foremost',inputFile,'-o','output'])
	for x in os.listdir('output/exe/'):
		y = os.path.getsize('output/exe/' + x)
		z = 'output/exe/'+x
		if y >= 200000:
			os.remove(z)
		elif y <= 2000:
			os.remove(z)
		else:
			continue
	for w in os.listdir('output/dll/'):
		y = os.path.getsize('output/dll/' + w)
		z = 'output/dll/'+w
		if y >= 200000:
			os.remove(z)
		elif y <= 2000:
			os.remove(z)
		else:
			continue
# MD5 Section
def md5():
	print 'Now running md5 against your output. Please wait.'
	subprocess.call(['md5 ' + 'output/exe/* ' + '>>' + ' MD5Text.txt'], 
					shell=True)
	subprocess.call(['md5 ' + 'output/dll/* ' + '>>' + ' MD5Text.txt'], 
					shell=True)
# Parse the file and begin checking each md5 against Virus Total
def vt():
	result = {}
	y = raw_input('Please paste your VT api key: ')
	with open('MD5Text.txt') as o:
		for line in o.readlines():
			if 'MD5' in line:
				key, value = line.split(' = ')
				result[key.strip(' ')] = value.strip('\n')
				fullResults = result
		o.close
		fullValues = fullResults.values()
	file = open('MaliciousFiles.txt','w')
	file.write('Below are the identified malicious files\n\n')
	file.close
	for x in fullValues:
		url = 'https://www.virustotal.com/vtapi/v2/file/report'
		parameters = {'resource': x, 'apikey': 
					y}
		data = urllib.urlencode(parameters)
		req = urllib2.Request(url, data)
		response = urllib2.urlopen(req)
		newResponse = response.read()
		print newResponse
		if '"positives": 0' in newResponse:
			print x + ' is not malicious'
		elif '"response_code": 0' in newResponse:
			print x + ' is not in VT'
		elif '"response_code": 1' in newResponse:
			print x + ' is a malicious file'
			file = open('MaliciousFiles.txt','a')
			file.write(x + ' is malicious ' + '\n\n' + newResponse + '\n')
			file.close
		else:
			print x + ' could not be searched. Please try again later.'
# check for no response due to API limitations.
		time.sleep(25)
# execute the program
if __name__ == '__main__':
	main()