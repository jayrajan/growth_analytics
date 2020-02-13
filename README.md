# GROWTH ANALYTICS - TWITTER SCHEDULER
This an automated twitter scheduler

The application is capable of the following:
* Reading tweets and image url's from a spreadsheet.
* Finding & Extracting the images from the url address.
* Fusing a company logo with the image
* The status and the images are uploaded and posted using twitter API
  every 5 seconds.

## PREREQUISITIE:
1. The program is scripted in Python3. Have the correct version of
   python installed.
2. Please ensure you have following libraries installed:
  * pandas
  * JSON
  * tweepy
  * urllib
  * re
  * os
3. Please have the following files in the same directory as core.py:
  * fuse_image.py (fusing image function)
  * GrowthAnalytics_python test_final.xlsx (main dataset containing)
  * test_core.py (Unit Tests)
4. Make sure the Twitter Key and Token are valid before running the script.
   Please update core.py file with the correct Security & Access Key/Token
   The code has been tested using my personal Twitter account and have been able
   post tweets.
5. If changing the Security & Access Key/Token, update this in the 'test_core.py'
   file. or else the unit test will fail.

## INSTRUCTIONS:
1. Please run script from a Terminal. Type python3 core.py
2. The code will prompt for the file name of the Excel spreadsheet. Key in
   GrowthAnalytics_python test_final.xlsx when asked.
3. There will be a new directory called 'fusion' which will contain copies
   of the url images with the hc logo.
4. The script is designed to post tweets every 5 seconds instead of 5 mins,
   This is for testing purposes. This can be tweaked in the core.py by
   adjusting the post_time variable in seconds.
5. Delete the fusion folder before running the script again.

## RUNNING THE TESTS:
Run the Unit Test by typing in the command python3 -m unittest test_core.py
###UNIT TESTS
Following Unit Test has been implemented:
1. Testing that the correct scheduler time value is used in variable
2. Testing that the correct excel file is captured
3. Testing the Twitter Consumer Key Token
4. Testing the Twitter Consumer Secret Token
5. Testing the Twitter Access Token
6. Testing the Twitter Access Secret Token
7. Testing the output response of the fuse logo function
8. Testing if the correct logo link is used on the images
9. Testing if the Json contains the item - post_ID
10. Testing if the Json contains the item - post_text
11. Testing if the Json contains the item - post_img

## Author
* Jerin Philips Rajan
