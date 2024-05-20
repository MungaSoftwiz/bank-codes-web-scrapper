from urllib.request import urlopen

url = "https://www.snowdesert.co.ke/resources/"

page_object = urlopen(url);

html_bytes = page_object.read();

html = html_bytes.decode('utf-8');

# print(html);

# find the title index

title = html.find("<title>");

# print(title);

# get the title text itself
start_index = html.find("<title>") + len("<title>");

last_index = html.find("</title>");

title_text = html[start_index:last_index];

print(title_text);

