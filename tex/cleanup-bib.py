import regex as re

path = "tex\\"
file_name = "skript"
extension = ".tex"

with open (path+"chapters\\" + 'Bibliography' + extension, 'r' ) as f:
    bib_file = f.read()
    bib = re.search(r'\\begin\{sphinxthebibliography\}\{(.*)\}((.|\n)*)', bib_file, flags = re.M).group(2)

    bib_items = re.split(r'(?=\\bibitem)', bib)

with open (path+'bibliography.bib', 'w' ) as f:   
    for m in bib_items:
        # match Author Name Year 
        entry_info = re.search(r'\\bibitem\[(.*)\]\{(.*)\}\n\\par\n(.*)\. \\emph\{(.*)\}\. (.*)\.(.*)', m)
        if not entry_info is None:
            entry_key = entry_info.group(1)
            entry_author = entry_info.group(3)
            entry_title = entry_info.group(4)
            entry_year = entry_info.group(5)

            if "," in entry_year:
                yp = re.split(r', ', entry_year)
                entry_publisher = yp[0]
                entry_year = yp[1]
            else:
                entry_publisher = ''

            if "." in entry_year:
                yp = re.split(r'. ', entry_year)
                entry_year = yp[0]


            f.write('\n@book{'+entry_key+',\n')
            f.write('    Author = {' + entry_author + '},\n')
            f.write('    year = {' + entry_year + '},\n')
            f.write('    title = {' + entry_title + '},\n')
            f.write('    publisher = {' + entry_publisher + '},\n}')