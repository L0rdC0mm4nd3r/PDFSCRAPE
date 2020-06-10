#!/usr/bin/python3
#you read codes huh? awesome <3
# -*- coding:utf-8 -*- 
# name   : PDFSCRAPE
# git    : http://github.com/L0rdC0mm4nd3r
# author : Lord Commander

from bs4 import BeautifulSoup
from urllib.request import urlopen
from tqdm import *
import urllib.request
import requests, time, os, sys, re

faculty  = {'BUISNESS AND ECONOMICS':['[1]Accounting and Finance----------------------------------------- http://196.189.45.87/handle/123456789/88193',
									  '[2]Business Administration and Information System----------------- http://196.189.45.87/handle/123456789/9',
									  '[3]Economics------------------------------------------------------ http://196.189.45.87/handle/123456789/87726',
									  '[4]Human Resources,Logistics and Supply Chain Management---------- http://196.189.45.87/handle/123456789/11',
									  '[5]Marketing and Management--------------------------------------- http://196.189.45.87/handle/123456789/12',
									  '[6]Public Administration and Development Management--------------- http://196.189.45.87/handle/123456789/87725'],
			'COMPUTING AND INFORMATICS':['[1]Computer Science-------------------------------------------- http://196.189.45.87/handle/123456789/88522'],
			'DEVELOPMENT STUDIES':['[1]Enviromental and Development Studies------------------------------ http://196.189.45.87/handle/123456789/24475',
								   '[2]Food Security Studies--------------------------------------------- http://196.189.45.87/handle/123456789/24476',
								   '[3]Gender Studies---------------------------------------------------- http://196.189.45.87/handle/123456789/24479',
								   '[4]Population Studies------------------------------------------------ http://196.189.45.87/handle/123456789/24480',
								   '[4]Regional and Local Development Studies---------------------------- http://196.189.45.87/handle/123456789/24486',
								   '[5]Rural Development Studies----------------------------------------- http://196.189.45.87/handle/123456789/24481'],
			'EDUCATIONAL AND BEHAVIOURAL STUDIES':['[1]Curriculum---------------------------------------- http://196.189.45.87/handle/123456789/15',
												   '[2]Education Planning and Management----------------- http://196.189.45.87/handle/123456789/16',
												   '[3]Psychology---------------------------------------- http://196.189.45.87/handle/123456789/17',
												   '[4]Special Needs------------------------------------- http://196.189.45.87/handle/123456789/18'],
			'GENERAL REFERENCE':['[1]Atlas--------------------------------------- http://196.189.45.87/handle/123456789/20',
								 '[2]Dictionaries-------------------------------- http://196.189.45.87/handle/123456789/21',
								 '[3]Encyclopedia-------------------------------- http://196.189.45.87/handle/123456789/22',
								 '[4]Handbooks----------------------------------- http://196.189.45.87/handle/123456789/23',
								 '[5]Reasearch----------------------------------- http://196.189.45.87/handle/123456789/24',
								 '[6]Subject Wise Reference---------------------- http://196.189.45.87/handle/123456789/25'],
			'HEALTH STUDIES':['[1]Biostatistics---------------------------------- http://196.189.45.87/handle/123456789/88423',
							  '[2]medical laboratory----------------------------- http://196.189.45.87/handle/123456789/30',
							  '[3]medicine--------------------------------------- http://196.189.45.87/handle/123456789/70',
							  '[4]pharmacy--------------------------------------- http://196.189.45.87/handle/123456789/28',
							  '[5]public health---------------------------------- http://196.189.45.87/handle/123456789/27'],
		    'HUMANITY,LANGUAGE STUDIES AND JOURNALISM':['[1]Foreign Language and Literature-------------------------- http://196.189.45.87/handle/123456789/1606',
		    											'[2]Journalism and Communication----------------------------- http://196.189.45.87/handle/123456789/1608',
		    											'[3]Linguistics---------------------------------------------- http://196.189.45.87/handle/123456789/1605'],
			'LAW AND GOVERNANCE STUDIES':['[1]Criminology--------------------------------- http://196.189.45.87/handle/123456789/87313',
										  '[2]Law----------------------------------------- http://196.189.45.87/handle/123456789/38',
										  '[3]Human Right--------------------------------- http://196.189.45.87/handle/123456789/37',
										  '[4]Federal Studies----------------------------- http://196.189.45.87/handle/123456789/36'],
			'NATURAL SCIENCE':['[1]Biology------------------------------------- http://196.189.45.87/handle/123456789/40',
							   '[2]Chemistry----------------------------------- http://196.189.45.87/handle/123456789/41',
							   '[3]Criminology Statistics---------------------- http://196.189.45.87/handle/123456789/87300',
							   '[4]Earth Sciences------------------------------ http://196.189.45.87/handle/123456789/42',
							   '[5]Enviromental Science------------------------ http://196.189.45.87/handle/123456789/64215',
							   '[6]Information and Computer Science------------ http://196.189.45.87/handle/123456789/43',
							   '[7]Mathematics--------------------------------- http://196.189.45.87/handle/123456789/44',
							   '[8]Physics------------------------------------- http://196.189.45.87/handle/123456789/45',
							   '[9]Sport Sciences------------------------------- http://196.189.45.87/handle/123456789/46',
							   '[10]Statistics--------------------------------- http://196.189.45.87/handle/123456789/47'],
			'PERFORMING AND VISUAL ARTS':['[1]Articles Performing and Visual Arts----------------------- http://196.189.45.87/handle/123456789/67810',
										  '[2]Fine Arts and Desgin-------------------------------------- http://196.189.45.87/handle/123456789/49',
										  '[3]Music----------------------------------------------------- http://196.189.45.87/handle/123456789/50',
										  '[4]Theatrical Arts------------------------------------------- http://196.189.45.87/handle/123456789/51'],
			'SOCIAL SCIENCE':['[1]African Studies----------------------------------------- http://196.189.45.87/handle/123456789/53',
							  '[2]Archeology and Heritage Management---------------------- http://196.189.45.87/handle/123456789/54',
							  '[3]Film and Televsion Production--------------------------- http://196.189.45.87/handle/123456789/79333',
							  '[4]Gender-------------------------------------------------- http://196.189.45.87/handle/123456789/1749',
							  '[5]Geographical Information Systems------------------------ http://196.189.45.87/handle/123456789/79337',
							  '[6]Geography----------------------------------------------- http://196.189.45.87/handle/123456789/1742',
							  '[7]History------------------------------------------------- http://196.189.45.87/handle/123456789/55',
							  '[8]Philosopy----------------------------------------------- http://196.189.45.87/handle/123456789/56',
							  '[9]Political science and international relation------------ http://196.189.45.87/handle/123456789/57',
							  '[10]Religion----------------------------------------------- http://196.189.45.87/handle/123456789/1748',
							  '[11]Social work-------------------------------------------- http://196.189.45.87/handle/123456789/58',
							  '[12]Sociology and Social Anthropology---------------------- http://196.189.45.87/handle/123456789/59'],
			'TECHNOLOGY':['[1]Architecture----------------------------------- http://196.189.45.87/handle/123456789/61',
						  '[2]Building Construction-------------------------- http://196.189.45.87/handle/123456789/62',
                          '[3]Chemical Engineering--------------------------- http://196.189.45.87/handle/123456789/63',
                          '[4]Civil Engineering------------------------------ http://196.189.45.87/handle/123456789/64',
                          '[5]Electrical and Computer Engineering------------ http://196.189.45.87/handle/123456789/65',
						  '[6]Industrial Engineering------------------------- http://196.189.45.87/handle/123456789/88582',
						  '[7]Material Engineering--------------------------- http://196.189.45.87/handle/123456789/88511',
                          '[8]Mechanical Engineering------------------------- http://196.189.45.87/handle/123456789/66',
                          '[9]Urban and Regional Planning-------------------- http://196.189.45.87/handle/123456789/67'],
			'VETERINARY MEDICINE':['[1]vVeterinary Medicine------------------------------ http://196.189.45.87/handle/123456789/69',
								   '[2]veterinary Medicine Collection-------------------- http://196.189.45.87/handle/123456789/1601',
								   '[3]Veterinary Collection I--------------------------- http://196.189.45.87/handle/123456789/34'],
			'LAND ADMINISTRATION':['[1]Land Administration------------------------------- http://196.189.45.87/handle/123456789/88869']					   
}
dep_main = ['BUISNESS AND ECONOMICS',
			'COMPUTING AND INFORMATICS',
			'DEVELOPMENT STUDIES',
			'EDUCATIONAL AND BEHAVIOURAL STUDIES',
			'GENERAL REFERENCE',
			'HEALTH STUDIES',
			'HUMANITY,LANGUAGE STUDIES AND JOURNALISM',
			'LAW AND GOVERNANCE STUDIES',
			'NATURAL SCIENCE',
			'PERFORMING AND VISUAL ARTS',
			'SOCIAL SCIENCE',
			'TECHNOLOGY',
			'VETERINARY MEDICINE',
			'LAND ADMINISTRATION']
			
faculty_choice = """
\033[1m\033[92m			               ______                                    
			    ____  ____/ / __/__________________ _____  ___  _____
\033[1m\033[93m			   / __ \/ __  / /_/ ___/ ___/ ___/ __ `/ __ \/ _ \/ ___/
			  / /_/ / /_/ / __(__  ) /__/ /  / /_/ / /_/ /  __/ /    
\033[1m\033[91m			 / .___/\__,_/_/ /____/\___/_/   \__,_/ .___/\___/_/     
			/_/                                  /_/                
			                     [~Made with <3 by Lord Commander~]\033[m 

\033[1m\033[92m
|~~~~~~~~~~1) BUISNESS AND ECONOMICS
|~~~~~~~~~~2) COMPUTING AND INFORMATICS
|~~~~~~~~~~3) DEVELOPMENT STUDIES
|~~~~~~~~~~4) EDUCATIONAL AND BEHAVIOURAL STUDIES
|~~~~~~~~~~5) GENERAL REFERENCE
|~~~~~~~~~~6) HEALTH STUDIES
|~~~~~~~~~~7) HUMANITY,LANGUAGE STUDIES AND JOURNALISM
|~~~~~~~~~~8) LAW AND GOVERNANCE STUDIES
|~~~~~~~~~~9) NATURAL SCIENCE
|~~~~~~~~~~10) PERFORMING AND VISUAL ARTS
|~~~~~~~~~~11) SOCIAL SCIENCE
|~~~~~~~~~~12) TECHNOLOGY
|~~~~~~~~~~13) VETERINARY MEDICINE
|~~~~~~~~~~14) LAND ADMINISTRATION\033[m
"""			

def link_crawler(link):
    try:
        website = 'http://196.189.45.87:80'
        alive = requests.head(link)

        if alive.status_code == 200:
            response = urlopen(link)
            soup = BeautifulSoup(response, "html.parser")
            links = soup.find_all('a')
            
            for link in links:
                link = link['href']
                page = 'page' in link
                offset = 'offset' in link
                num_filter = str(re.search(r'\d+$',link))

                if link.startswith('/handle') and num_filter != None and link.endswith('num_filter') == False and offset == False and page == False:
                    link = website+link
                    if link not in pdf_link:
                        pdf_link.append(link)
                    else:pass
                    
                if link.startswith('/handle') and num_filter != None and link.endswith('num_filter') == False and offset == True:
                    link = website+link
                    if link not in next_link:
                        next_link.append(link)
                    else:pass

    except OSError:
        exit('\033[1m\033[91m[!]No internet connection!\033[m')
    except KeyboardInterrupt:
        exit('\033[1m\033[91m[!]Exiting!\033[m')


def downloadlink(link):
	try:
	    website = 'http://196.189.45.87:80'
	    alive = requests.head(link)

	    if alive.status_code == 200:
	        response = urlopen(link)
	        soup = BeautifulSoup(response, "html.parser")
	        links = soup.find_all('a')
	        
	        for link in links:
	            link = link['href']
	            if link.startswith('/bitstream'):
	                link = website+link
	                if link not in download_link:
	                    download_link.append(link)
	                else:pass
	except OSError:
		exit('\033[1m\033[91m[!]No internet connection!\033[m')
	except KeyboardInterrupt:
		exit('\033[1m\033[91m[!]Exiting!\033[m')


def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size )
    speed = int(progress_size/(1024 * duration))
    percent = int(count * block_size * 100/total_size)
    sys.stdout.write('\r\033[1m\033[92mDownloading PDF--------------------------------------------------%d%%,%d MB,%d KB/s,%d seconds elapsed\033[m'%
                    (percent,progress_size/(1024 * 1024),speed, duration))
    sys.stdout.flush()



def main(dep_link):
	try:
		count = 0
		download_tracker = 0
		link_crawler(dep_link)

		for i in tqdm(range(215),unit='page',desc='\033[1m\033[92m[~]Extracting PDF links from pages\033[m'):
		    try:
		        link_crawler(next_link[len(next_link)-1])    
		    except IndexError:
		        pass
		print('\033[1m\033[94m[*]Extracted %s PDF links\033[m' % len(pdf_link))

		for i in tqdm(range(len(pdf_link)),unit='link',desc='\033[1m\033[92m[~]Extracting Download link from PDF links\033[m'):
		    count += 1
		    lpd = int(len(pdf_link)+count-len(pdf_link))
		    downloadlink(pdf_link[lpd-1])
		print('\033[1m\033[94m[*]I found %s PDFs\n\033[m'%len(download_link))
		for i in download_link:
			filename = i.split('/1/',1)[1]

			try:
				check_download = open('download.log','r')
				check_download = check_download.read()

				if filename in check_download:
					print('\033[1m\033[91m[!]%s already Exists!\033[m'% filename)
					pass
				else:
					urllib.request.urlretrieve(i,filename,reporthook)
					print('\n\033[1m\033[92m[*]%s Downloaded!' % filename)
					check_download = open('download.log','a')
					check_download.write(filename+'\n')
					download_tracker+=1
					if download_tracker == len(download_link):
						os.remove('download.log')
						

			except FileNotFoundError:
				check_download = open('download.log','a')
				check_download.write(filename+'\n')
				urllib.request.urlretrieve(i,filename,reporthook)
				print('\n\033[1m\033[92m[*]%s Downloaded!' % filename)

				download_tracker+=1
				if download_tracker == len(download_link):
					os.remove('download.log')
	except OSError:
		exit('\033[1m\033[91m[!]No internet connection!\033[m')
	except KeyboardInterrupt:
		exit('\033[1m\033[91m[!]Exiting!\033[m')


def choice():
	try:
		print(faculty_choice)
		select_dept = int(input('[~]Select faculty: '))
		choice = dep_main[select_dept-1]
		print('\033[1m\033[94m[*]You selected %s\n\033[m' % choice)
		time.sleep(2)
		print('\n'.join(faculty[choice]))
		select_div = int(input('\n[~]Select your department: '))
		div_choice = faculty[choice][select_div-1]
		choice = div_choice.split('- ',1)[1]    
		main(choice)

	except IndexError:
		exit('\033[1m\033[91m[!]Not found!\033[m')
	except ValueError:
		exit('\033[1m\033[91m[!]Invalid input!\033[m')
	except KeyboardInterrupt:
		exit('\033[1m\033[91m[!]Exiting!\033[m')

download_link = []       
pdf_link = []
next_link = []


if __name__ == '__main__':
	choice()
