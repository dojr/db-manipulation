DROP TABLE IF EXISTS beer_comp;
DROP TABLE IF EXISTS brewery_comp;
DROP TABLE IF EXISTS style;
DROP TABLE IF EXISTS category;

CREATE TABLE `brewery_comp`(
  `id`INT(11) AUTO_INCREMENT,
  `name` VARCHAR(255),
  PRIMARY KEY (`id`)
);

CREATE TABLE `category`(
  `id` INT(11) AUTO_INCREMENT,
  `name` VARCHAR(255),
  PRIMARY KEY(`id`)
);

CREATE TABLE `style`(
  `id` INT(11) AUTO_INCREMENT,
  `cat_id` INT(11),
  `name` VARCHAR(255),
  PRIMARY KEY(`id`),
  FOREIGN KEY(`cat_id`) REFERENCES `category`(`id`)
);

CREATE TABLE `beer_comp` (
  `id` INT(11) AUTO_INCREMENT,
  `brewery_id`INT(11),
  `name` VARCHAR(255),
  `cat_id` INT(11),
  `style_id` INT(11),
  `abv` FLOAT(4),
  `ibu` INT(11),
  `description` VARCHAR(4096),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`brewery_id`) REFERENCES `brewery_comp` (`id`),
  FOREIGN KEY (`cat_id`) REFERENCES `category` (`id`),
  FOREIGN KEY(`style_id`) REFERENCES `style` (`id`)
);

LOAD DATA LOCAL INFILE
'/home/donald/projects/brewjay_dev/db_manipulation/compare_brew/categories.csv'
INTO TABLE category
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE
'/home/donald/projects/brewjay_dev/db_manipulation/compare_brew/styles.csv'
INTO TABLE style
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE
'/home/donald/projects/brewjay_dev/db_manipulation/compare_brew/breweries.csv'
INTO TABLE brewery_comp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE
'/home/donald/projects/brewjay_dev/db_manipulation/compare_brew/beers.csv'
INTO TABLE beer_comp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
