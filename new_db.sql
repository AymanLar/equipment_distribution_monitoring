CREATE DATABASE IF NOT EXISTS equipment_monitoring ;
USE equipment_monitoring ;
CREATE TABLE distributions (
  distribution_id INT AUTO_INCREMENT,
  date DATE,
  livreur VARCHAR(255),
  receptionnaire VARCHAR(255),
  commune_sce VARCHAR(255),
  dp_div VARCHAR(255),
  aref_dir VARCHAR(255),
  observation TEXT,
  telephone VARCHAR(255),
  email VARCHAR(255),
  photos_avant TEXT,
  photos_apres TEXT,
  PRIMARY KEY (distribution_id)
);

CREATE TABLE devices (
  device_id INT AUTO_INCREMENT,
  distribution_id INT,
  ref VARCHAR(255),
  destination VARCHAR(255),
  cycle VARCHAR(255),
  livre_par VARCHAR(255),
  receptionne_par VARCHAR(255),
  fonction VARCHAR(255),
  demande VARCHAR(255),
  photos_avant TEXT,
  photos_apres TEXT,
  PRIMARY KEY (device_id),
  FOREIGN KEY (distribution_id) REFERENCES distributions(distribution_id)
);

 ALTER TABLE devices ADD COLUMN name VARCHAR(255) NOT NULL;
