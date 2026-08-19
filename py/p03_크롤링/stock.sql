CREATE SCHEMA `stock` ;

use stock;

CREATE TABLE `stock`.`daily_market` (
  `dt` DATE NULL,
  `seq` INT NOT NULL AUTO_INCREMENT,
  `item_name` VARCHAR(100) NULL,
  `item_code` VARCHAR(100) NULL,
  `price` BIGINT NULL,
  `foreign_ownership_ratio` FLOAT NULL,
  `rel_return` FLOAT NULL,
  `per` FLOAT NULL,
  `per_12m` FLOAT NULL,
  `per_ind` FLOAT NULL,
  `pbr` FLOAT NULL,
  `dividend_yield` FLOAT NULL,
  `volume` BIGINT NULL,
  `trans_price` BIGINT NULL,
  `market_capital_prefer` BIGINT NULL,
  `market_capital_common` BIGINT NULL,
  PRIMARY KEY (`seq`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

select * from daily_market;