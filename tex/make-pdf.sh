echo
echo WARNING - still requires one manual quit of first pdf/latex pass, use shift-x to quit
echo

jupyter-book build . --builder latex

cp ./_build/latex/skript.tex ./tex/

python ./tex/cleanup-tex.py