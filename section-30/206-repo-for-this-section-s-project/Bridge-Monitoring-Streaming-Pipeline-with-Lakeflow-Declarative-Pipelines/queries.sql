--landing
SELECT * FROM delta.`/Volumes/bridge_monitoring/00_landing/streaming/bridge_temperature/`;
SELECT * FROM delta.`/Volumes/bridge_monitoring/00_landing/streaming/bridge_tilt/`;
SELECT * FROM delta.`/Volumes/bridge_monitoring/00_landing/streaming/bridge_vibrations/`;

--bronze
SELECT * FROM bridge_monitoring.`01_bronze`.bridge_temperature ORDER BY event_time DESC;
SELECT * FROM bridge_monitoring.`01_bronze`.bridge_tilt ORDER BY event_time DESC;
SELECT * FROM bridge_monitoring.`01_bronze`.bridge_vibration ORDER BY event_time DESC;

--silver
SELECT * FROM bridge_monitoring.`02_silver`.bridge_temperature ORDER BY event_time DESC;
SELECT * FROM bridge_monitoring.`02_silver`.bridge_tilt ORDER BY event_time DESC;
SELECT * FROM bridge_monitoring.`02_silver`.bridge_vibration ORDER BY event_time DESC;

--gold
SELECT * FROM bridge_monitoring.`03_gold`.bridge_metrics ORDER BY window_start DESC;