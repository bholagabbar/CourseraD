# coursera-download-script
A Python script to download all the videos for a course you are currently enrolled in from the new [Coursera 2016 website](https://www.coursera.org/)

#####Requirements: Linux system (Windows instructions at the end), Python 2.7, pip, Selenium, Chromedriver (already included)

*Get Python 2.7 [here](https://www.python.org/downloads/release/python-2712/)*<br>
*Getting pip:* `sudo apt-get install python pip`<br>
*Getting Selenium* `sudo pip install selenium`<br>

####Instructions:

 1. Open up `cr_down.py` in your favourite text editor (eg: `gedit cr_down.py` for n00bs)
 2. Enter your details in line 9-19. These include your **username**, **password**, **enrolled course link**, **directory to store** and **wait parameter** (optional. you should be fine with relatively fast internet. Incase of slow internet, increase it in multiples of 5)
 3. Save and close. Incase you simply want to test the script, comment the lines 74 - 77
 4. Once you're ready, uncomment, save and run (`python cr_down.py`). A browser window will open. *Mute the tab (or your computer), minimize the browser windows and let the script run in peace. Or don't minimize it and watch the download in process. Gets kinda boring after a while*. Oh, and be patient :innocent: (And don't press a single button on any of the pages that open, the script will most likely crash because *you* interfered)

#####To get this to run on Windows, install the same dependencies, download *chromedriver.exe* and change line 4 to `driver = webdriver.Chrome(executable_path=os.getcwd()+'\\chromedriver.exe')`. You'll also have to run through the code once and make the directories you wish to store the videos in are valid

######Feel free to contribute. Pull Requests, new features etc are welcome
