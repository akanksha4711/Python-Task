# Python-Task
Web Scraping using bs4

This application scrapes data from urls of the type "https://www.amazon.{country}/dp/{asin}".
It reads url from a csv file and stores data in .json file.
The data includes product title, image url, price and details.

I used bs4 because it is beginner freindly and given the time constrains seemed like a good choice.

Approach
I first wrote code for a single url. I learnt how to use bs4 for web scraping. Once I was able to produce the required result I wrote 3 seperate programs: one to read data from a csv file, second for error handling in case of invalid url, third for writing data to a .json file.
I combined the code into the main file and reproduced the original results.

Challenges and Improvments 
The main challenge I faced during development was scaling the program to run on larger data set.
I still need to improve the number of urls that can be processed. At present the programs can scrape only a few urls at a time. I had to create the .json output file by rerunning the code multiple times. For some reason it does not scrape data from all valid urls in a single run for larger input data.

Running the program
- An empty 'result.json' file must be present in the same directory when running 'my-web-s.py' for the first time
