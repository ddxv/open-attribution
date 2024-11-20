CREATE MATERIALIZED VIEW installs_base_mv
REFRESH EVERY 5 SECOND
TO installs_base AS
WITH
    installs AS (
        SELECT 
            *,
            MIN(event_time) OVER (
                PARTITION BY oa_uid,
                        ifa
                ) AS install_time
        FROM 
            events
        WHERE 
            event_id = 'app_open'
    )
SELECT 
    install_time,
    store_id,
    event_id,
    ifa,
    oa_uid,
    client_ip,
    event_uid,
    received_at
FROM installs;