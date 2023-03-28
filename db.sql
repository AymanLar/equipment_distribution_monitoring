CREATE DATABASE IF NOT EXISTS equipment_monitoring ;
USE equipment_monitoring ;
CREATE TABLE equipment (
  id INT PRIMARY KEY AUTO_INCREMENT,
  date DATE,
  unite_centrale INT,
  ecran INT,
  printer INT,
  video_projecteur INT,
  destination VARCHAR(255),
  cycle VARCHAR(255),
  livre_par VARCHAR(255),
  receptionne_par VARCHAR(255),
  fonction VARCHAR(255),
  demande VARCHAR(255),
  telephone VARCHAR(255),
  email VARCHAR(255),
  photos_avant VARCHAR(255),
  photos_apres VARCHAR(255),
  commune VARCHAR(255),
  DP VARCHAR(255),
  AREF VARCHAR(255),
  observation VARCHAR(255)
);

