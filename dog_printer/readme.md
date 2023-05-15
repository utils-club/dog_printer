# dog

## escenario

se está usando dolibarr como plataforma de punto de pago y se tiene localmente un computador linux (lubuntu 23.04) y una impresora termica xprinter XP-58, al usar el boton de imprimir ticket en el punto de venta de dolibarr la impresora termica imprime caracteres irreconocibles, sin embargo, la impresora es capaz de imprimir correctamente archivos pdf.

## hipotesis de solucion

se plantea guardar el archivo en una carpeta como pdf, una vez el archivo esté guardado, se puede imprimir como un pdf normal

## funcionalidad

este script vigila la carpeta Descargas y si en ella se crea el archivo recipe.php.pdf  creado por dolibarr al tratar de imprimir un ticket y guardarlo como archivo pdf, el archivo recipe.php.pdf es renombrado y mandado a imprimir en una impresora termica.

## instalacion

revisar el script dog.py y revisar:

- el nombre de la impresora termica cups es correcto en su caso
- puede cambiar el nombre de la compañia por el propio
- puede cambiar el nombre de la carpeta que se vigila

luego, puede crear un ambiente virtual y ejecutar el archivo dog.py para cerciorarse de su correcto funcionamiento

para que el archivo funcione permanentemente en su sistema, ejecutar el archivo install.sh, este le mostrará un texto que debe usar para ponerlo en su sistema operativo como una operación/accion al inicio, de esta manera el programa empezará a funcionar apenas encienda su equipo

## notas

- probado en lubuntu 23.04, xubuntu 22.10