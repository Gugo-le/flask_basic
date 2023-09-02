-- Active: 1693581595587@@127.0.0.1@3306@mysql
CREATE TABLE songtest(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    duration INT,
    file_path VARCHAR(255)
);

INSERT INTO songtest (title, artist, album, duration, file_path) VALUES ('시든 꽃이 물을 주듯', 'Hion', '600', 210, '/Users/gugo-le/Desktop/ML/voicemodel/hion/600/hion._시든 꽃이 물을 주듯.wav');
INSERT INTO songtest (title, artist, album, duration, file_path) VALUES ('잊어야 한다는 마음으로', 'Hion', '600', 265, '/Users/gugo-le/Desktop/ML/voicemodel/hion/600/hion._잊어야 한다는 마음으로.wav');

SELECT * FROM songtest;