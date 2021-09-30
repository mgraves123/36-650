ALTER TABLE player_bios
ADD COLUMN position TEXT;

UPDATE player_bios
SET position = new_table.position
FROM new_table
WHERE id = player;


select id,firstname,lastname,position from player_bios limit 5;