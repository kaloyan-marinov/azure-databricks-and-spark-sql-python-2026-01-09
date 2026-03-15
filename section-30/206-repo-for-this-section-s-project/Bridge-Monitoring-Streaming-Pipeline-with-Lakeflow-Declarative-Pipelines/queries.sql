-- Inspect the `00_landing` zone.
SELECT
    *
FROM
    delta.`/Volumes/bridge_monitoring/00_landing/streaming/bridge_temperature/`
;

SELECT
    *
FROM
    delta.`/Volumes/bridge_monitoring/00_landing/streaming/bridge_tilt/`
;

SELECT
    *
FROM
    delta.`/Volumes/bridge_monitoring/00_landing/streaming/bridge_vibrations/`
;



-- Inspect the `01_bronze` zone.
SELECT
    *
FROM
    bridge_monitoring.`01_bronze`.bridge_temperature
ORDER BY
    event_time DESC
;

SELECT
    *
FROM
    bridge_monitoring.`01_bronze`.bridge_tilt
ORDER BY
    event_time DESC
;

SELECT
    *
FROM
    bridge_monitoring.`01_bronze`.bridge_vibration
ORDER BY
    event_time DESC
;



-- Inspect the `02_silver` zone.
SELECT
    *
FROM
    bridge_monitoring.`02_silver`.bridge_temperature
ORDER BY
    event_time DESC
;

SELECT
    *
FROM
    bridge_monitoring.`02_silver`.bridge_tilt
ORDER BY
    event_time DESC
;

SELECT
    *
FROM
    bridge_monitoring.`02_silver`.bridge_vibration
ORDER BY
    event_time DESC
;



-- Inspect the `03_gold` zone.
SELECT
    *
FROM
    bridge_monitoring.`03_gold`.bridge_metrics
ORDER BY
    window_start DESC
;
