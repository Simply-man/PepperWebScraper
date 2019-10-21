echo off
title: Pepper Deals to CSV

rem Going to folder where we have PepperWebScraper project
cd /D "PATH"

rem Active virtualenv
call Scripts\activate.bat

rem Going into folder with our spider
cd /D "LOCATION FOR SCRAPER ON YOUR COMPUTER"

rem Calling "scrapy" to save data form web into json file
call scrapy crawl -o js.json pepper

rem Going to folder when we have file witch can convert our json file into CSV
cd /D "PATH"

rem Calling script with activate comprasion from json to CSV
call python JsonToCSV.py

rem Closing script
call exit()