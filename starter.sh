echo -n "¿Desea ejecutar el programa? [S/N] : "
read resultado

if [[ $resultado == ["Ss"] ]]; then
    clear
    chmod u+x starter_mac.py
    python starter_mac.py
else
    echo "No se ha instalado el programa"
fi