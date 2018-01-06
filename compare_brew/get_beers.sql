-- I started with my original list of breweries and compared the names
-- of another brewery list I found that was also connected to a beers table.
-- I used a select statement to get the connected beers and replaced
-- the brew_id's with the original table that I created.

  CREATE TABLE `beer` (
    `id` INT(11) AUTO_INCREMENT,
    `brew_id`INT(11),
    `name` VARCHAR(255),
    `cat_id` INT(11),
    `style_id` INT(11),
    `abv` FLOAT(4),
    `ibu` INT(11),
    `description` VARCHAR(4096),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`brew_id`) REFERENCES `brewery` (`id`),
    FOREIGN KEY (`cat_id`) REFERENCES `category` (`id`),
    FOREIGN KEY(`style_id`) REFERENCES `style` (`id`)
  )
  SELECT b.id AS brew_id, bc.name, bc.cat_id, bc.style_id, bc.abv, bc.ibu, bc.description FROM brewery_comp
  INNER JOIN brewery b ON brewery_comp.name = b.name
  INNER JOIN beer_comp bc ON brewery_comp.id = bc.brewery_id;
