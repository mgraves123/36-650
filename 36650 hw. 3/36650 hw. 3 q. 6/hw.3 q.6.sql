ALTER TABLE player_bios
ADD COLUMN inches integer;

UPDATE player_bios
SET inches=12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

ALTER TABLE player_bios
DROP COLUMN height;

ALTER TABLE player_bios
RENAME COLUMN inches to height;

select firstname,lastname,height from player_bios limit 5;