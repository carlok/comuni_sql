CREATE TABLE IF NOT EXISTS regioni (
id int(11) NOT NULL auto_increment,
nome varchar(100) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
CREATE TABLE IF NOT EXISTS province (
id int(11) NOT NULL auto_increment,
nome varchar(100) NOT NULL,
id_regione int(11) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (id_regione) REFERENCES regioni(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
 
CREATE TABLE IF NOT EXISTS comuni (
id int(11) NOT NULL auto_increment,
nome varchar(100) NOT NULL,
id_provincia int(11) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (id_provincia) REFERENCES province(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;