# RedBubble-Web-Scrapper
 A Python Script I created to automate coding for the shopping page of rosebud-textiles

<b> Instructions: </b>
- open the script and input the link into the script


<b> pull the source code from the webpage and print it to the console: </b>
```python

# request the input of the url to parse
print('Enter the URL:')
x = input()
print('Extracting Source code from: ' + x) 

# pull the source code from the page
opener = urllib.request.FancyURLopener({})
url = x
webpage = opener.open(url)
content = webpage.read()

# test print of code that was extracted
print(content)

```

<b> create an html file to save the source code: </b>
```python

# create a html file to save the code
html_file = open("source.html", "w")
html_file.write(str(content) + "\n")
html_file.close()

```

<b> create a text file to store a list of what content you are scraping for: </b>
- in this instance I was searching for specific links of products
  - I wanted any links that was a string between these two strings
    - "<a data-testid="available-product" href=""
    - " element="a" class="styles__link--3QJ5N">"
```python

# create a list to save links for available products and pass it into a text file
links_file = open("links.txt", "w")
link_list = re.findall('<a data-testid="available-product" href="(.+?)" element="a" class="styles__link--3QJ5N">', str(content))

# test print of list of links
#print(*link_list)

links = '\n'.join(map(str,link_list))
links_file.write(links)
links_file.close()

```

most of the rest of this code is specialized to write my html for the website
