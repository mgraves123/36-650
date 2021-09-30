CREATE TABLE new_table (
	player INTEGER REFERENCES more_player_stats,
	prl NUMERIC,
	POSITION TEXT
);

insert into new_table (player, prl) (select id,round(per - 67*va/(gp*minutes), 1) from more_player_stats);

UPDATE new_table
SET position = 'PF'
WHERE prl>11.3;

UPDATE new_table
SET position = 'PG'
WHERE 10.7<prl and prl<11.3;

UPDATE new_table
SET position = 'SG/SF'
WHERE 10.5<prl and prl<10.8;

UPDATE new_table
SET position = 'PG'
WHERE -.1<prl and prl<10.6;

UPDATE new_table
SET position = '??'
WHERE 0>prl;


select * from new_table limit 10;