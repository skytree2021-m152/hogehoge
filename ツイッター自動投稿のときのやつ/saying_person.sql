DROP TABLE IF EXISTS saying_person;
CREATE TABLE saying_person (
    id      INTEGER UNIQUE PRIMARY KEY,
    name    VARCHAR(64)
);

INSERT INTO saying_person ( id, name ) VALUES ( 1, 'ガンジー' );
INSERT INTO saying_person ( id, name ) VALUES ( 2, '福沢諭吉' );
INSERT INTO saying_person ( id, name ) VALUES ( 3, '渋沢栄一' );
INSERT INTO saying_person ( id, name ) VALUES ( 4, 'アインシュタイン' );
