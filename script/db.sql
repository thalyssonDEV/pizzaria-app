CREATE TABLE funcionario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL
);


CREATE TABLE pizza (
    tipo VARCHAR(100) NOT NULL
);


CREATE TABLE preco (
    tamanho VARCHAR(10) NOT NULL,
    preco FLOAT NOT NULL
);