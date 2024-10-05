"""
File: webcrawler.py
Name: Ocean
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {
            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}
        response = requests.get(url, headers=header)
        html = response.text
        soup = BeautifulSoup(html)
        # ----- Write your code below this line ----- #
        tags = soup.find_all('tbody')
        male_count = 0
        female_count = 0
        for tag in tags:
            tokens = tag.text.split()
            for i in range(0, 1000, 5):
                number1 = ''
                number2 = ''
                for ch in tokens[i+2]:
                    if ch is not ',':   # Remove ',' from number
                        number1 += ch
                for ch in tokens[i+4]:
                    if ch is not ',':   # Remove ',' from number
                        number2 += ch
                male_count += int(number1)
                female_count += int(number2)
        print('Male Number: ' + str(male_count))
        print('Female Number: ' + str(female_count))


if __name__ == '__main__':
    main()
