/*
Tables:
	client
    shopper
    store
    shoppingList
    shoppingCart
    inventory
*/

USE project;

CREATE TABLE client (
	ClientID				Integer				NOT NULL AUTO_INCREMENT,
	ClientFirstName			Char(35)			NOT NULL,
	ClientLastName			Char(35)			NOT NULL,
	CONSTRAINT			Client_PK			PRIMARY KEY(ClientID)
	);
    