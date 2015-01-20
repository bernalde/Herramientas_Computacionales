wget https://raw.githubusercontent.com/jngaravitoc/HerramientasComputacionales/master/Lectures/2.Unix-TextEditors/Hands-on/Sainte-Beuve.txt

echo El numero de veces que se repite A es:
grep -o -i a Sainte-Beuve.txt | wc -l 
echo El numero de veces que se repite E es:
grep -o -i e Sainte-Beuve.txt | wc -l 
echo El numero de veces que se repite I es:
grep -o -i i Sainte-Beuve.txt | wc -l 
echo El numero de veces que se repite O es:
grep -o -i o Sainte-Beuve.txt | wc -l 
echo El numero de veces que se repite U es:
grep -o -i u Sainte-Beuve.txt | wc -l 
