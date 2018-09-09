#Käyttöohje, ominaisuudet, puuttuvat ominaisuudet ja rajoitteet 
Sovellus löytyy [Herokusta](). Paikalliseen käyttöön löytyy asennusohjeet [täältä]().

##Kirjautuminen
Sisäänkirjautuminen onnistuu pääkäyttäjätunnuksilla (_Kirjaudu sisään_):
```
käyttäjätunnus: hello
salasana: world
```

Uloskirjautuminen onnistuu milloin tahansa (_Kirjaudu ulos_). 

##Omat kurssit 
Sisäänkirjautunut käyttäjä ohjataan aluksi omien kurssien listaukseen (_Omat kurssit_). Listauksesta on tarkoitus päästä kurssikohtaiselle sivulle, joka vaihtelee käyttäjäroolin mukaan, mutta toiminnallisuutta ei ole vielä toteutettu.

##Käyttäjien hallinta
Järjestelmään voi lisätä erilaisia käyttäjiä (_Lisää käyttäjä_). Mahdolliset vaihtoehdot ovat pääkäyttäjä, opettaja ja oppilas. Käyttäjälle täytyy määritellä 5-50 merkkiä pitkä nimi, käyttäjätunnus ja salasana sekä käyttäjärooli pudotusvalikosta. Tällä hetkellä ainoastaan pääkäyttäjä voi lisätä käyttäjiä. Muokkaus- ja poistotoiminnallisuutta ei ole toteutettu.

##Kurssien hallinta
Kursseilla on täysi CRUD-ominaisuus, joka on suojattu siten, että vain pääkäyttäjät pääsevät siihen käsiksi. Tällä hetkellä kurssien lisäys on toteutettu omalla sivulla (_Lisää kurssi_ ), josta pääkäyttäjä ohjataan uuden kurssin lisäyksen myötä automaattisesti kurssilistaukseen. Kurssilistauksen yhteydessä on toetutettu kurssien hallinta (_Kurssien hallinta_). Kursseja voi muokata ja poistaa. Lisäksi kurssille voidaan lisätä käyttäjiä. Tällä hetkellä käyttäjien lisäys onnistuu yksi kerrallaan pudotusvalikon kautta. Uusien kurssien lisäys on validoitu siten, että kurssinimen on oltava 5-50 merkkiä pitkä. Kurssien muokkausta ei kuitenkaan ole vielä validoitu, joten se pitäisi korjata.

##Kysymysten hallinta
Myös kysymyksillä on täysi CRUD-ominaisuus. Polut on suojattu niin, että vain opettajat pääsevät niille. Sovellukseen pitäisi vielä korjata, koska nyt opettajat pääsevät muokkaamaan ja poistamaan toistensa kysymyksiä. Myös kysymysten lisäys on toteutettu omalla sivulla (_Lisää kysymys_), josta siirrytään automaattisesti kysymyslistaukseen. Kysymyslistauksen yhteydessä kysymyksiä voi muokata ja poistaa (_Kysymysten hallinta_). Myös kysymysten lisäys on validoitu siten, että kysymyksen on oltava 1-50 merkkiä pitkä. Myös muokkauksen validointi tulisi toetuttaa. Kysymykset on tarkoitus liittää kursseihin, mutta sitä ei ole vielä toteutettu.

##Kyselyn täyttäminen
Kyselyn on suojattu siten, että vain opiskelijat pääsevät täyttämään sen (_Täytä kysely_). Vastauksen on oltava 1-50 merkkiä pitkä. Tällä hetkellä jokainen tallenna-painallus tallentaa uuden vastauksen tietokantaan. Opiskelija ei voi poistaa tai muokata vastauksia. Tällä hetkellä vastauksen voi tallentaa yksi kerrallaan. Vastaus on liitetty kysymykseen ja takoitus olisi toteuttaa sivu, jossa opettaja pääsee tarkastelemaan kysymyskohtaisia vastauksia.