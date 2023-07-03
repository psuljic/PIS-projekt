# PIS-projekt

POKRETANJE PROJEKTA
1. Unutar working direktorija otvorimo terminal
2. Naredbom "docker build -t flask ." pokrenemo docker image
3. Napišemo u bilo kojem browseru "localhost:5000" te vidimo da aplikacija radi
4. Pomoću alata "Postman" (ili sličnog) možemo isprobati da li rade ostale CRUD operacije

MOGUĆNOSTI 
1. Ispis svih predmeta u wishlist-i (localhost:5000/wishlist) [GET]
2. Dodavanje novog predmeta (localhost:5000/wishlist) [POST]
3. Update predmeta (localhost:5000/wishlist/{id}) [PUT]
4. Brisanje predmeta (localhost:5000/wishlist/{id}) [DELETE]
5. Ispis jednog predmeta (localhost:5000/wishlist/{id}) [GET]
