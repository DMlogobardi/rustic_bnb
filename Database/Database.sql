DROP DATABASE IF EXISTS BnB;
CREATE DATABASE IF NOT EXISTS BnB;
USE BnB;

CREATE TABLE utente (
    id int AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(13) NOT NULL UNIQUE,
    password VARCHAR(13) NOT NULL,
    data_nascita DATE NOT NULL,
    gender CHAR(1) NOT NULL DEFAULT "F",
    n_c VARCHAR(16) NOT NULL,
    admin CHAR(1) NOT NULL DEFAULT "n"
);

INSERT INTO utente (username, password, gender, data_nascita, n_c, admin)
VALUES ("gestore","admin","m","2004-06-23","784569","Y");

CREATE TABLE offerte_prezzi(
    id int AUTO_INCREMENT PRIMARY KEY,
    data_in DATE,
    data_out DATE UNIQUE,
    prezzo_offerta DECIMAL NOT NULL,
    min_person int DEFAULT 1
);

INSERT INTO offerte_prezzi (prezzo_offerta) 
VALUES ("50");

CREATE TABLE prenotazioni(
    id int AUTO_INCREMENT PRIMARY KEY, 
    fk_utente int NOT NULL UNIQUE,
    fk_offerte int NOT NULL UNIQUE,
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    cost DECIMAL NOT NULL,
    FOREIGN KEY (fk_utente) REFERENCES utente(id),
    FOREIGN KEY (fk_offerte) REFERENCES offerte_prezzi(id)
);