#Tietokantarakenne

###Tietokannanhallintajärjestelmä
Paikallisesti käytössä on SqLite ja palvelimella (Heroku) postgresql.

###Tietokantakaavio
<img src= "https://github.com/idaliisa/kurssikysely/blob/master/documentation/pictures/tietokantakaavio.png">

###CREATE TABLE -lauseet
CREATE TABLE IF NOT EXISTS "Kurssi" (
        id INTEGER NOT NULL,
        nimi VARCHAR(500) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS "Kayttaja" (
        id INTEGER NOT NULL,
        nimi VARCHAR(150) NOT NULL,
        kayttajatunnus VARCHAR(150) NOT NULL,
        salasana VARCHAR(150) NOT NULL,
        kayttajatyyppi VARCHAR(150) NOT NULL,
        PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS "Kysymys" (
        id INTEGER NOT NULL,
        kysymys VARCHAR(500) NOT NULL,
        kurssi_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(kurssi_id) REFERENCES "Kurssi" (id)
);
CREATE TABLE IF NOT EXISTS "KurssiKayttaja" (
        kurssi_id INTEGER NOT NULL,
        kayttaja_id INTEGER NOT NULL,
        PRIMARY KEY (kurssi_id, kayttaja_id),
        FOREIGN KEY(kurssi_id) REFERENCES "Kurssi" (id),
        FOREIGN KEY(kayttaja_id) REFERENCES "Kayttaja" (id)
);
CREATE TABLE IF NOT EXISTS "Vastaus" (
        id INTEGER NOT NULL,
        vastaus VARCHAR(500) NOT NULL,
        kysymys_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(kysymys_id) REFERENCES "Kysymys" (id)
);