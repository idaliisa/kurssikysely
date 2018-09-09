### Ennen asennusta
Asennusta on testattu MacOs käyttöjärjestelmällä.
Käytössä tulee olla python3, pip, venv-kirjasto, heroku, sqlite3 ja PostgreSQL.

# Asennus paikallisesti

### Kloonaa projekti haluamaasi kansioon seuraavalla komennolla
```
git clone git@github.com:idaliisa/kurssikysely.git
```

### Luo virtuaaliympäristö ja aktivoi se.
```
cd kurssikysely
python3 -m venv venv
source venv/bin/activate
```

### Lataa riippuvuudet
```
pip install -r requirements.txt
```

### Käynnistä sovellus
````
python3 run.py
````

### Lisää pääkäyttäjä tietokantaan polussa kurssikysely/application/
```
sqlite3 questions.db
INSERT INTO 'Kayttaja' (nimi, kayttajatunnus, salasana, kayttajatyyppi) values ('hello world', 'hello', 'world', 'paakayttaja');
```

### Mene selaimella osoitteeseen http://localhost:5000/. Käyttöohjeet löytyvät [täällä](https://github.com/idaliisa/kurssikysely/blob/master/documentation/kayttoohje.md).

### Svelluksen sammutus komennolla ctrl+C


# Asennus palvelimelle (Heroku)
Tässä oletetaan että virtuaaliympäristö on aktiivinen ja riippuvuudet on ladattu (kts. asennus paikallisesti). Muista myös kirjautua herokuun ensin.

### Luo sovellukselle paikka herokuun

```
heroku create uniikkinimi
```
Huom. Komentoriviltä näet sovelluksen osoitteen

### Lisää paikalliseen versionhallintaan tieto Herokusta

```
git remote add heroku https://git.heroku.com/uniikkinimi.git
git add .
git commit -m "sovellus Herokuun"
git push heroku master
```

### Lisää Herokuun tietokanta
```
heroku config:set HEROKU=1
heroku addons:add heroku-postgresql:hobby-dev
```

### Lisää tietokantaan pääkäyttäjä
```
heroku pg:psql
INSERT INTO "Kayttaja" (nimi, kayttajatunnus, salasana, kayttajatyyppi) values ('hello world', 'hello', 'world', 'paakayttaja');
```
