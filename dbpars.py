import os
import logging
import time


parsdb = open('parsdb.txt','w+')
parsdb.close()
parsdb = open('parsdb.txt','a+')
filecat = input('Путь к папке: ')
fileNameFilter = input('Расширение файлов с паролями: ')
myDBList = os.listdir(filecat)
myDBString = '\n'.join(myDBList)
replaceyml = myDBString.replace(fileNameFilter,':')

logging.basicConfig(filename="sample.log", level=logging.DEBUG)
logging.debug("\nDebug: \n" + time.ctime() + '\n')
logging.info("\nInformational: \n" + time.ctime()+ '\n')
logging.error("\n!!!ERROR!!!: \n" + time.ctime()+ '\n')
a = 0
def aplus():
    global a
    a += 1

def parspass():
	file_name = 'upload.txt'
	dirname = filecat
	try:
		for file_name in os.listdir(dirname):
			with open(os.path.join(dirname, file_name), 'r') as file:
				while True:
					aplus()
					passfile = open(filecat+'/'+str(myDBList[a]),'r')
					passline = passfile.readlines()
					print(myDBList[a].replace(fileNameFilter, ':' + passline[1].replace('password: ','')))
					parsdb.write(myDBList[a].replace(fileNameFilter, ':' + passline[1].replace('password: ','')))
					passfile.close()
					continue
	except IndexError:
		print('\nБаза выгружена!\nВ файле dbpars.txt появились логины:пароли')




parspass()
