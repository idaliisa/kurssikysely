# Käyttötapaukset ja niihin liittyvät SQL-kyselyt

###Kaikki käyttäjät
* Pääkäyttäjä/Opettaja/Opiskelija voi kirjautua järjestelmään sisään. Opettajan/Opiskelijan sisäänkirjautuminen edellyttää, etää pääkäyttäjä on luonut tunnukset. Sisäänkirjautunut käyttäjä ohjataan ensimmäiseksi sivulle, jossa hänen kurssinsa näkyvät. Järjestelmästä pääsee myös kirjautumaan ulos. TOTEUTETTU

###Pääkäyttäjä
* Pääkäyttäjä voi lisätä, poistaa ja muokata kaikkia kursseja. Hän voi myös lisätä kurssille opiskelijoita ja opettajia. TOTETUTETTU

```
INSERT INTO "Kurssi" (nimi) VALUES (?)
```

```
DELETE FROM "KurssiKayttaja"
DELETE FROM "Kurssi" WHERE "Kurssi".id = ?
````

```
UPDATE "Kurssi" SET nimi=? WHERE "Kurssi".id = ?
````

```
INSERT INTO "KurssiKayttaja" (kurssi_id, kayttaja_id)
```

###Opettaja
* Opettaja voi lisätä, muokata ja poistaa kysymyksiä. TOTEUTETTU

```
INSERT INTO "Kysymys" (kysymys, kurssi_id) VALUES (?, ?)
```

```
UPDATE "Kysymys" SET kysymys=? WHERE "Kysymys".id = ?
```

```
DELETE FROM "Kysymys" WHERE "Kysymys".id = ?
```

* Opettaja voi tarkastella kyselyn vastauksia ja saada yhteenvetotietoja (vastanneiden lukumäärä). 

###Opiskelija
* Opiskelija voi vastata kurssikyselyyn. TOTEUTETTU

````
INSERT INTO "Vastaus" (vastaus, kysymys_id) VALUES (?, ?)
```