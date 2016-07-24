from selenium import webdriver
import os, time, urllib

driver = webdriver.Chrome(executable_path=os.getcwd()+'/chromedriver')

driver.get('https://www.coursera.org/?authMode=login')

# ENTER Credentials
email = 'xxx@yyy.zz'
password = 'yourPassword'
# ENTER Course Name you are ALREADY ENROLLED (videos should be visible) **IN SAME FORMAT BELOW**
course_link = 'https://www.coursera.org/learn/ml-foundations'
# ENTER start and end week
start_week = 1
end_week = 6
# ENTER valid directory for storing vids weekwise. Make sure you don't need sudo
store_dir = '/home/YOUR_USERNAME/Desktop'
#Enter implicit wait time parameter. Lesser foren faster internet. If the script crashes because of 'could not find on page' or something, increase this
wait_time = 5

### That's about it. Now run this script and if it doesn't have fun debugging it. Buhbye

course_name = course_link[course_link.find('learn') + 6 :]
store_dir += '/' + course_name

time.sleep(wait_time/2)

email_in = driver.find_element_by_name("email")
password_in = driver.find_element_by_name("password")

email_in.send_keys(email)
password_in.send_keys(password)

button = driver.find_element_by_css_selector('#rendered-content > div > div:nth-child(1) > div.rc-AuthenticationModal > div > div.c-modal-content > div > div > div > form > button')
button.click()

for wi in range (start_week, end_week + 1):
	driver.get(course_link+'/home/week/'+str(wi)) 
	time.sleep(wait_time * 2)

	no_of_headings=len(driver.find_elements_by_css_selector('div.od-lesson-collection-element > div:nth-child(1) > div:nth-child(1) > h4:nth-child(1)'))
	lim = no_of_headings #set no of headings

	headings = []

	print "week: " + str(wi), "\nheadings: " + str(lim)
	for i in range(1 ,lim+1):
		headings.append('#rendered-content > div > div.rc-OndemandApp > div > div > div.rc-HomeLayoutBody > main > div > div.rc-PeriodPage > div.horizontal-box.wrap > div > section > div.rc-ModuleLessons > div > div > div > div:nth-child('+ str(i) +')> div > div > h4')
		folder_name = driver.find_element_by_css_selector(headings[i-1]).text
		print folder_name
		
		newpath = store_dir + '/w'+str(wi) + '/' + folder_name 
		if not os.path.exists(newpath):
		    os.makedirs(newpath)

		dalink=driver.find_elements_by_css_selector('#rendered-content > div > div.rc-OndemandApp > div > div > div.rc-HomeLayoutBody > main > div > div.rc-PeriodPage > div.horizontal-box.wrap > div > section > div.rc-ModuleLessons > div > div > div > div:nth-child('+str(i)+') > div > span > a')

		link_list=[]
		for x in dalink:
			try:
				xx = x.get_attribute('href')
				link_list.append(xx)
			except Exception, e:
				print e
				continue

		for to_link in link_list:
			if to_link.find('lecture') > 0:
				topic = to_link[to_link.rfind('/') + 1:]
				print topic
				'''To avoid downloading and just checking if the script works (print topics weekwise and heading wise)
				Comment the 4 lines below'''
				#From here
				driver.get(to_link)
				time.sleep(wait_time * 2)
				vid_link = driver.find_element_by_css_selector('.rc-LectureDownloadItem > a:nth-child(1)').get_attribute('href')
				urllib.urlretrieve(vid_link, newpath + "/" + topic+".mp4")
				#Till here
		print '\n\n'
		driver.get(course_link+'/home/week/'+str(wi))
		time.sleep(wait_time * 1.8)
