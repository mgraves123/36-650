DROP TABLE rdata;

CREATE TABLE rdata(
id SERIAL PRIMARY KEY,
a TEXT UNIQUE NOT NULL CHECK (char_length(a)<6),
b TEXT UNIQUE NOT NULL CHECK (char_length(b)<6),
moment DATE DEFAULT '2020-01-01'::DATE,
x NUMERIC(5,2) CHECK (x>0)
);
