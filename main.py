### generates the HTML for a given list of elements for the tier list ###

# attached style.css and script.js are required

def key_imports():
    global tiers #imports tiers and items from text file
    tiers = []
    with open('tiers.txt', 'r') as f:
        tiers = f.read().splitlines() 

    global items
    items = []
    with open('items.txt', 'r') as f:
        for i in f.readlines():
            items.append(i.split("-"))

def save_html(name, html):
    with open(f'{name}.html','a') as f:
            f.write(html)

start_html ="""
<!DOCTYPE html>
<html>
  <head>
    <title>Tierlist!</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <p>try not to drag items ontop of each other! (you can drag them out of each other) to reset press ctrl+R, to export as pdf use the print to pdf function after pressing ctrl+P! 🏳️‍⚧️🏳️‍🌈<br>
      made by <a href="https://www.bellatrix.dev"> bellatrix / rose</a><br> 
      not mobile friendly at all sry</p>
"""

end_html= """
<br>
<p>thank you for using this tierlist! :D</p>
</body>
</html>
"""

dropzone_template = """<div class="dropzone" ondragover="onDragOver(event);" ondrop="onDrop(event);">{}<br></div>"""

draggable_template = """<div id="{item_text}" draggable="true" ondragstart="onDragStart(event);" class="draggable" > {item_text} </div>"""


key_imports()
for tier in tiers:
    start_html += dropzone_template.format(tier)

temp_items = ""
for item in items:
    temp_items += draggable_template.format(item_text=item[0].replace("\n",""))

start_html += dropzone_template.format(temp_items)
start_html += end_html
save_html(input("name the file\t>\t"), start_html)