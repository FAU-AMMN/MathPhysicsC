import regex as re

path = "tex\\"
file_name = "skript"
extension = ".tex"

def match_theorems(content):
    keys = {'Example': 'example', 'Definition':'definition', 'Theorem':'theorem', 'Remark':'remark', 
            'note': 'emphBox', 'danger': 'emphBox', 'Lemma': 'lemma'}
    token_init = r'\\begin\{sphinxadmonition\}\{note\}\{'
    token_end = r'\\end\{sphinxadmonition\}'
    
    
    for key in keys:
        # case 1: theorem has title text
        content = re.sub(token_init + key + r' .\.. ([^\}]*?)\}((.|\n)*?)' + token_end, 
                             r'\\begin{' + keys[key] + r'}{}{\1}\2\\end{'+keys[key]+'}', content, flags = re.M)
    	# case 2: no title text
        content = re.sub(token_init + key + r' (.*?)\}((.|\n)*?)' + token_end, 
                             r'\\begin{' + keys[key] + r'}{}{}\2\\end{'+keys[key]+'}', content, flags = re.M)

    # add all labels in a second run
    for key in keys:
        content = re.sub(r'\\label\{(.*?)\}\n\\begin\{'+ keys[key] + r'\}\{(.*?)\}\{(.*?)\}', 
                             r'\\begin{' + keys[key] + r'}{\3}{\1}', content, flags = re.M)
    
    # note boxes
    content = re.sub(r'\\begin\{sphinxadmonition\}\{danger\}\{(.*?)\}((.|\n)*?)' + token_end, 
                             r'\\begin{' + keys['danger'] + r'}{}{}\2\\end{'+keys['danger']+'}', content, flags = re.M)
    # note boxes
    content = re.sub(r'\\begin\{sphinxadmonition\}\{note\}((.|\n)*?)' + token_end, 
                             r'\\begin{' + keys['note'] + r'}{}{}\1\\end{'+keys['note']+'}', content, flags = re.M)
    
    content = re.sub(r'\\begin\{sphinxShadowBox\}\n\\(.*?)stylesidebartitle\{(.*?)\}((.|\n)*?)\\end\{sphinxShadowBox\}', 
                             r'\\begin{' + keys['note'] + r'}{\2}{}\3\\end{'+keys['note']+'}', content, flags = re.M)
    return content

def match_proofs(content):
    content = re.sub(r'\\begin\{emphBox\}\{\}\{\}\nProof\.((.|\n)*?)\\end\{emphBox\}', 
                     r'\\begin{proof}\n\1\\end{proof}', content, flags = re.M)
    content = re.sub(r'\\begin\{emphBox\}\{\}\{\}\n\\AtStartPar\nProof\.((.|\n)*?)\\end\{emphBox\}', 
                     r'\\begin{proof}\n\1\\end{proof}', content, flags = re.M)
    return content


def replace_tabular(m):
    tab_id = '|'
    for i in range(len(re.findall('\|',  m.group(3))) - 1):
        tab_id += 'c|'
    
    return '\\begin{tabularx}{\linewidth}' + '[' + m.group(1) + ']' + '{' + tab_id + '}'

def replace_underscore(m):
    s = m.groups(1)[0]
    return r'\includegraphics[width=\textwidth]{' + re.sub(r'_', r'\\string_', s, flags = re.M) + r'}'

def graphics(content):
    # replace optional arguments
    content_new =  re.sub(r'\\includegraphics\[(.*?)]\{(.*?)\}', r'\\includegraphics{\2}', content, flags = re.M)

    file_ending = '(.png|.jpg)'
    # path specification
    content_new = re.sub(r'\\includegraphics\{\{(.*?)\_build\/jupyter\_execute(.*?)\\(.*?)\}'+file_ending+'\}',
                         r'\\includegraphics{\3\4}', content_new, flags = re.M)
    content_new = re.sub(r'\\includegraphics\{\{(.*?)\_build\/jupyter\_execute(.*?)/(.*?)\}'+file_ending+'\}',
                         r'\\includegraphics{\3\4}', content_new, flags = re.M)

    content_new = re.sub(r'\\includegraphics\{\{(.*?)\}'+file_ending+'\}',
                         r'\\includegraphics{\1\2}', content_new, flags = re.M)

    content_new = re.sub(r'\\includegraphics\{(.*?)'+file_ending+'\}',
                         r'\\includegraphics{../_build/html/_images/\1\2}', content_new, flags = re.M)
    content_new = re.sub(r'\\includegraphics\{(.*?)\}', replace_underscore, content_new, flags = re.M)
    return content_new


with open (path+file_name+extension, 'r' ) as f:
    content = f.read()
    
    
    # preamble
    content_new = re.sub(r'\\sphinx(.*?)', r'\\\1', content, flags = re.M)
    
    # graphics
    content_new = graphics(content_new)
    
                   
    # Misc
    content_new = re.sub(r'\\capstart', r'', content_new, flags = re.M) 
    content_new = re.sub(r'\\hyphen{}', r' ', content_new, flags = re.M)
    content_new = re.sub(r'\\styleemphasis', '\\emph', content_new, flags = re.M)
    content_new = re.sub(r'\\styleemphasis', '\\emph', content_new, flags = re.M)
    content_new = re.sub(r'\\newcommand\{\\logo\}\{\\vbox\{\}\}', '', content_new, flags = re.M)
    content_new = re.sub(r'\\makeindex', '', content_new, flags = re.M)
    content_new = re.sub(r'\\maketitle', '', content_new, flags = re.M)
    content_new = re.sub(r'\\tableofcontents', '', content_new, flags = re.M)
    content_new = re.sub(r'\\unicode\{(.*?)\}', r'\\symbol{"\1}', content_new, flags = re.M)
    content_new = re.sub(r'\\code\{(.*?)\}', r'{\1 broken reference}', content_new, flags = re.M)
    
    # theorems and proofs
    content_new = match_theorems(content_new)
    content_new = match_proofs(content_new)
    
    # tables
    content_new = re.sub(r'\\begin\{savenotes\}\\attablestart((.|\n)*?)\\par\n\\attableend\\end\{savenotes\}', 
                         r'\\begin{center}\1\\end{center}', content_new, flags = re.M)
    
    # remove splits
    content_new = re.sub(r'\\begin\{split\}((.|\n)*?)\\end\{split\}', 
                         r'\1', content_new, flags = re.M)
    content_new = re.sub(r' \n\\end\{equation\*\}', 
                         r'\\end{equation*}', content_new, flags = re.M)

    # replace every equation by align
    content_new = re.sub(r'\\begin\{equation', r'\\begin{align', content_new, flags = re.M)
    content_new = re.sub(r'\\end\{equation', r'\\end{align', content_new, flags = re.M)
    
    # remove verbatim
    content_new = re.sub(r'\\begin\{sphinxVerbatim\}((.|\n)*?)\\end\{sphinxVerbatim\}', 
                         r'', content_new, flags = re.M)
    
    # references
    content_new = re.sub(r'\{\\hyperref\[\\detokenize\{(.*?)\}\]\{\\crossref\{(.*?)\}\}\}(( |.)|\n)',
                         r'\\cref{\1} ', content_new, flags = re.M)
    
    content_new = re.sub(r'\{tabulary\}', r'{tabularx}', content_new, flags = re.M)
    content_new = re.sub(r'\{tabular\}', r'{tabularx}', content_new, flags = re.M)
    
    # content_new = re.sub(r'\\begin\{tabularx\}\[(.*?)\]\{(.*?)\}', 
    #                      r'\\begin{tabularx}{\\textwidth}[\1]{\2}', content_new, flags = re.M)
    

    # lists
    content_new = re.sub(r'\\setlistlabels\{\\arabic\}\{enumi\}\{enumii\}\{\}\{\.\}\%', r'', content_new, flags = re.M)
    
    
    content_new = re.sub(r'\\begin\{tabularx\}(.*?)\[(.*?)\]\{(.*?)\}\n', replace_tabular, content_new, flags=re.M)
        
    content_new = re.sub(r'stylestrong', 'textbf', content_new, flags=re.M)
    
    # remove index 
    content_new = re.sub(r'\\begin\{sphinxtheindex\}((.|\n)*?)\\end\{sphinxtheindex\}', 
                         r'', content_new, flags = re.M)
    content_new = re.sub(r'\\printindex', r'', content_new, flags = re.M)

    # bibtex citations
    content_new = re.sub(r'\{\[\}\\hyperlink\{(.*?)\}\{(.*?)\}\{\]\}', r'\\cite{\2}', content_new, flags = re.M)
    
    # Par
    content_new = re.sub(r'\\AtStartPar', r'\\par', content_new, flags = re.M)
    
    
    
    # get rid of certain commands
    content_new = re.sub(r'\\release\{\}', r'', content_new, flags = re.M)
    content_new = re.sub(r'\\renewcommand\{\\releasename\}\{\}', r'', content_new, flags = re.M)
    content_new = re.sub(r'\\phantomsection', r'', content_new, flags = re.M)
    content_new = re.sub(r'\\styletheadfamily', r'', content_new, flags = re.M)
    content_new = re.sub(r'\\pagestyle\{(.*?)\}', r'', content_new, flags = re.M)
    content_new = re.sub(r'\\DUrole{xref,myst}{}',r'', content_new, flags = re.M)
    content_new = re.sub(r'\\upquote\{(.*?)\}',r'\1', content_new, flags = re.M)
    
    # Umlaute
    special = {'ß':'\ss{}', 'ä':'\"a', 'ü':'\"ü', 'ö':'\"ü'}

    # replacements for intro
    content_new = re.sub(r'\\begin\{DUlineblock\}\{0em\}\n\\item\[\] \\textbf\{\\Large (.*?)\}\n\\end\{DUlineblock\}', 
                         r'\\subsection{\1}', content_new, flags = re.M)

    content_new = re.sub(r'\\begin\{sphinxVerbatimOutput\}((.|\n)*?)\\end\{sphinxVerbatimOutput\}', 
                         r'\1', content_new, flags = re.M)
     
    
# split up into chapters
chapters = []

m_chapters = re.split(r'(?=\\chapter)', content_new)


for i, m in enumerate(m_chapters):
    if i == 0:
        chapter_name = "intro"
        m = re.search(r'\\begin\{document\}((.|\n)*)', m, flags = re.M).group(1)
        m = '\chapter{Vorwort}\n' + m
    else:
        chapter_name = re.search(r'\\chapter\{(.*?)\}', m)
        if not chapter_name is None:
            chapter_name = chapter_name.group(1)

    if not chapter_name is None:
        chn = re.sub(r' ',r'', chapter_name, flags = re.M)
        chn = re.sub(r'ß',r'ss', chn, flags = re.M)
        with open(path+"chapters\\" + chn + extension, "w") as text_file:
            text_file.write(m)
            chapters.append(chn)

content_main = re.search(r'((.|\n)*?)\\begin\{document\}', content_new, flags = re.M)
with open(path+file_name+"_clean"+extension, "w") as text_file:    
    text_file.write('\\input{preamble}\n')
    #text_file.write(content_main.group(1))
    text_file.write('\\begin{document}\n')
    text_file.write('\\frontmatter\n')
    text_file.write('\\maketitle\n')  
    text_file.write('\\tableofcontents\n')
    text_file.write('\\input{chapters/intro}\n') 
    text_file.write('\\mainmatter\n')
    for ch in chapters:
        if not ch in ["intro", "Bibliography"]:
            text_file.write('\\input{chapters/'+ch+'}\n')  
    
    text_file.write('\\backmatter\n')
    text_file.write('\\printbibliography\n')
    text_file.write('\\end{document}') 
    
with open(path+file_name+"_ref"+extension, "w") as text_file:
    text_file.write(content_new) 

    