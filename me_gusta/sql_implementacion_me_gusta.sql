-- -----------------------------------------------------
-- Implementación me gusta y propuesta de mejora
-- -----------------------------------------------------
-- Selección de la base de datos habi 
USE `habi_db` ;

-- Creación de la tabla `city`
CREATE TABLE IF NOT EXISTS `habi_db`.`city` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`id`))
  ENGINE = InnoDB;
  
-- Inserción de las ciudades que se encuentran en la tabla property 
-- a la tabla city, realizando un ajuste en formato
INSERT INTO `habi_db`.`city`(name) 
SELECT DISTINCT UPPER(RTRIM(city)) as city
FROM property
where RTRIM(city) <> ''
order by city;

-- Agregar la columna city_id a la tabla property
ALTER TABLE property
ADD `city_id` INT(11) NOT NULL,
ADD CONSTRAINT `fk_Property_city`
FOREIGN KEY (`city_id`)
REFERENCES `habi_db`.`city` (`id`);

-- Se agregó los Ids correspondientes a las ciudades en la tabla property
SET SQL_SAFE_UPDATES = 0;
UPDATE  `habi_db`.`property` p
JOIN `habi_db`.`city` c ON UPPER(RTRIM(p.city)) = c.name
SET p.city_id = c.id;
SET SQL_SAFE_UPDATES = 1;

-- Eliminación de la columna city de la tabla property
ALTER TABLE property
DROP COLUMN city;  

-- Creación de la tabla `user`
CREATE TABLE IF NOT EXISTS `habi_db`.`user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(15) NOT NULL,
  `email` VARCHAR(75) NOT NULL,
  `password` VARCHAR(10) NOT NULL,
  `city_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_User_city1_idx` (`city_id` ASC) VISIBLE,
  CONSTRAINT `fk_User_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `habi_db`.`city` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
    ENGINE = InnoDB;


-- Creación de la tabla `habi_db`.`like_history`
CREATE TABLE IF NOT EXISTS `habi_db`.`like_history` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `update_date` DATETIME NOT NULL,
  `property_id` INT(11) NOT NULL,
  `user_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Likes_property1_idx` (`property_id` ASC) VISIBLE,
  INDEX `fk_like_history_user1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_Likes_property1`
    FOREIGN KEY (`property_id`)
    REFERENCES `habi_db`.`property` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_like_history_user1`
    FOREIGN KEY (`user_id`)
    REFERENCES `habi_db`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
    ENGINE = InnoDB;
    
