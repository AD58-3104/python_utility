from html.parser import HTMLParser
import sys
from bs4 import BeautifulSoup


if len(sys.argv) < 3:
    print("please input target html filename & target folder!!")
    exit()

target_html_file = sys.argv[1]

file = open(target_html_file,'r')
html_text_data = file.read()
file.close()

parser = BeautifulSoup(html_text_data, 'html.parser')

folders = parser.find_all('h3')
folder_no = 0
for itm in folders:
    if itm.text in sys.argv[2]:
        break
    folder_no += 1

output_bookmarks = parser.find_all('dl')
parsed_text = str(output_bookmarks[folder_no+1])
output_file = open('parsed_html.html','w')
output_file.write(parsed_text)
output_file.close()