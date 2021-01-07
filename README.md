# SOE-ProgAlap1-Beadando-Simon-Marton

A program egy 4X4-es Táblázatban egy 2048-as játékot takar, amelyben a w/a/s/d gombok lenyomásával, valamint az "exit", parancsszóval tudjuk irányítani a dolgokat.
Ha az "save" parancsszót kapja meg a program, az automatikus elmentést jelent egy Json fájlba, melyet későbbi ujrabetöltéssel lehet folytatni.
# A Működési elvek:

A játék folyamatosan jelzi a játékosnak a pontot  és a táblázatot.
A működés a megszokott módon történik:
Ha a játékos eléri a 2048-at akkor nyert, egészen addig random üresen maradt helyekre spawnolnak 2-esek amikkel lehet építkezni a cél felé.
Ha a játékos a 2048 elérése előtt fut ki a helyből az Game Overt jelent

# A program felépítése:

A program modulokból és egy fómodulból áll, melyben az előre megírt függvények vannak meghívva.
Minden függvény rendelkezik teszttel, és az egész program dokumentálvva van html-formátumban pdoc3 használatával
