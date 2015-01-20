#Punto 1 Taller 3 David Bernal 200921359 Herramientas Computacionales

#Importación del archivo de datos
wget https://raw.githubusercontent.com/jngaravitoc/HerramientasComputacionales/master/Homeworks/HW3/ggiro.csv

#Ajuste del archivo de datos y paso al archivo .tex
sed 's/$/\\\\ \\hline/g' ggiro.csv>ggiro.tex
sed 's/,/ \&/g' ggiro.tex>ggiro1.tex
sed 's/"//g' ggiro1.tex>giro.tex

#Borrar lor archivos intermedio
rm ggiro.csv ggiro.tex ggiro1.tex

emacs punto1.tex &

printf "%s" "\documentclass[8pt]{article}
\usepackage[hmargin=2.0cm,vmargin=1cm]{geometry}
\usepackage{float}
\begin{document}
\begin{table}[h]
\centering
\begin{tabular}{|c|c|c|c|c|c|c|c|c|}
\hline
"> punto1.tex

cat giro.tex>>punto1.tex

printf "%s" "\end{tabular}
\end{table}
\end{document}" >> punto1.tex

latex punto1.tex
pdflatex punto1.tex
evince punto1.pdf &
