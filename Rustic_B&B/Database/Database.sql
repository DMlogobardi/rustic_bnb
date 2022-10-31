DROP DATABASE IF EXISTS BnB;
CREATE DATABASE IF NOT EXISTS BnB;
USE BnB;

CREATE TABLE utente (
    id int AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(13) NOT NULL,
    password VARCHAR(13) NOT NULL,
    data_nascita DATE NOT NULL,
    gender CHAR(1) NOT NULL DEFAULT "F",
    n_c VARCHAR(16) NOT NULL,
    admin CHAR(1) NOT NULL DEFAULT "n",
);

INSERT INTO utente (username, password, gender, data_nascita, cf, admin)
VALUES ("gestore","admin","m","2004-06-23","LNNGTT04H23C235H","Y");

CREATE TABLE prenotazioni(
    id int AUTO_INCREMENT PRIMARY KEY, 
    fk_utente INT NOT NULL UNIQUE,
    fk_offerte INT NOT NULL UNIQUE,
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    cost DECIMAL NOT NULL,  
);

CREATE TABLE offerte(
    id int AUTO_INCREMENT PRIMARY KEY,
    data_in DATE NOT NULL,
    data_out DATE NOT NULL,
    offerta DECIMAL NOT NULL,
    max_person int NOT NULL DEFAULT 1
);
