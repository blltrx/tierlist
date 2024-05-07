### generates the HTML for a given list of elements for the tier list ###

# attached style.css and script.js are required

START_HTML: str ="""
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

END_HTML= """
<br>
<p>thank you for using this tierlist! :D</p>
</body>
</html>
"""

DROPZONE_TEMPLATE = """<div class="dropzone" ondragover="onDragOver(event);" ondrop="onDrop(event);">{}<br></div>"""

DRAGGABLE_TEMPLATE = """<div id="{item_text}" draggable="true" ondragstart="onDragStart(event);" class="draggable" > {item_text} </div>"""

    
def key_imports() -> tuple[list[str], list[str]]:
    tiers = []
    with open('tiers.txt', 'r') as f:
        tiers = f.read().splitlines() 

    items = []
    with open('items.txt', 'r') as f:
        for i in f.readlines():
            items.append(i.split("-"))

    return tiers, items

def save_html(name: str, html: str):
    with open(f'{name}.html','a') as f:
            f.write(html)


def main():
    global START_HTML
    tiers, items = key_imports()
    for tier in tiers:
        START_HTML += DROPZONE_TEMPLATE.format(tier)

    temp_items = ""
    for item in items:
        temp_items += DRAGGABLE_TEMPLATE.format(item_text=item[0].replace("\n",""))

    START_HTML += DROPZONE_TEMPLATE.format(temp_items)
    START_HTML += END_HTML
    save_html(input("name the file\t>\t"), START_HTML)

if __name__ == "__main__":
    main()
