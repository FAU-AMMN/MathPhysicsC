import regex as re

path = "tex\\"
file_name = "skript"
extension = ".tex"

def match_theorems(content):
    keys = {'Example': 'example', 'Definition':'definition', 'Theorem':'theorem', 
            'note': 'emphBox', 'Lemma': 'lemma'}
    token_init = r'\\begin\{sphinxadmonition\}\{note\}\{'
    token_end = r'\\end\{sphinxadmonition\}'
    
    
    for key in keys:
        content = re.sub(token_init + key + r' (.*?)\}((.|\n)*?)' + token_end, 
                             r'\\begin{' + keys[key] + r'}{}{}\2\\end{'+keys[key]+'}', content, flags = re.M)
    
    # note boxes
    content = re.sub(r'\\begin\{sphinxadmonition\}\{note\}((.|\n)*?)' + token_end, 
                             r'\\begin{' + keys['note'] + r'}{}{}\1\\end{'+keys['note']+'}', content, flags = re.M)
    
    content = re.sub(r'\\begin\{sphinxShadowBox\}\n\\(.*?)stylesidebartitle\{(.*?)\}((.|\n)*?)\\end\{sphinxShadowBox\}', 
                             r'\\begin{' + keys['note'] + r'}{\2}{}\3\\end{'+keys['note']+'}', content, flags = re.M)
    return content

def match_proofs(content):
    content = re.sub(r'\\begin\{emphBox\}\{\}\{\}\nProof\.((.|\n)*?)\\end\{emphBox\}', 
                     r'\\begin{proof}\n\1\\end{proof}', content, flags = re.M)

    return content


def replace_tabular(m):
    tab_id = '|'
    for i in range(len(re.findall('\|',  m.group(3))) - 1):
        tab_id += 'c|'
    
    return '\\begin{tabularx}{\linewidth}' + '[' + m.group(1) + ']' + '{' + tab_id + '}'

with open (path+file_name+extension, 'r' ) as f:
    content = f.read()
    
    
    # preamble
    content_new = re.sub(r'\\sphinx(.*?)', r'\\\1', content, flags = re.M)
    
    # graphics
    #content_new = re.sub(r'\\noindent\\includegraphics\{(.*?)\}\n', r'', content_new, flags = re.M)
    
    content_new = re.sub(r'\\noindent{\\hspace\*\{\\fill\}\\includegraphics\{(.*?)\}\\hspace\*\{\\fill\}\}',
                         r'', content_new, flags = re.M)
    
    # Misc
    content_new = re.sub(r'\\hyphen{}', r' ', content_new, flags = re.M)
    content_new = re.sub(r'\\styleemphasis', '\\emph', content_new, flags = re.M)
    content_new = re.sub(r'\\styleemphasis', '\\emph', content_new, flags = re.M)
    content_new = re.sub(r'\\newcommand\{\\logo\}\{\\vbox\{\}\}', '', content_new, flags = re.M)
    content_new = re.sub(r'\\makeindex', '', content_new, flags = re.M)
    content_new = re.sub(r'\\maketitle', '', content_new, flags = re.M)
    content_new = re.sub(r'\\tableofcontents', '', content_new, flags = re.M)
    
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
    content_new = re.sub(r'\{\\hyperref\[\\detokenize\{(.*?)\}\]\{\\crossref\{(.*?)\}\}\}',
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
    
    # get rid of certain commands
    content_new = re.sub(r'\\release\{\}', r'', content_new, flags = re.M)
    content_new = re.sub(r'\\renewcommand\{\\releasename\}\{\}', r'', content_new, flags = re.M)
    content_new = re.sub(r'\\phantomsection', r'', content_new, flags = re.M)
    content_new = re.sub(r'\\styletheadfamily', r'', content_new, flags = re.M)
    content_new = re.sub(r'\\pagestyle\{(.*?)\}', r'', content_new, flags = re.M)
    
    # Umlaute
    special = {'ß':'\ss{}', 'ä':'\"a', 'ü':'\"ü', 'ö':'\"ü'}
     
    

chapters = []

m_chapters = re.split(r'(?=\\chapter)', content_new)


for m in m_chapters:
    chapter_name = re.search(r'\\chapter\{(.*?)\}', m)
    if not chapter_name is None:
        chapter_name = chapter_name.group(1)
        with open(path+"chapters\\" + chapter_name + extension, "w") as text_file:
            text_file.write(m)
            chapters.append(chapter_name)

content_main = re.search(r'((.|\n)*?)\\begin\{document\}', content_new, flags = re.M)
with open(path+file_name+"_clean"+extension, "w") as text_file:    
    text_file.write('\\input{preamble}\n')
    #text_file.write(content_main.group(1))
    text_file.write('\\begin{document}\n')
    text_file.write('\\frontmatter\n')
    text_file.write('\\maketitle\n')  
    text_file.write('\\tableofcontents\n')
    text_file.write('\\mainmatter\n')
    for ch in chapters:
      text_file.write('\\input{chapters/'+ch+'}\n')  
    
    text_file.write('\\end{document}') 
    
with open(path+file_name+"_ref"+extension, "w") as text_file:
    text_file.write(content_new) 

    
