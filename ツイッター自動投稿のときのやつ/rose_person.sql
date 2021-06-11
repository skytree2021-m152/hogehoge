DROP TABLE IF EXISTS rose_person;
CREATE TABLE rose_person (
    id      INTEGER UNIQUE PRIMARY KEY,
    name    VARCHAR(64)
);

INSERT INTO rose_person ( id, name ) VALUES ( 1, '水銀燈' );
INSERT INTO rose_person ( id, name ) VALUES ( 2, '金糸雀' );
INSERT INTO rose_person ( id, name ) VALUES ( 3, '翠星石' );
INSERT INTO rose_person ( id, name ) VALUES ( 4, '真紅' );
INSERT INTO rose_person ( id, name ) VALUES ( 5, '雪華綺晶' );
INSERT INTO rose_person ( id, name ) VALUES ( 6, 'その他' );