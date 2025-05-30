CREATE MATERIALIZED VIEW user_daily_events_attributed_mv 
REFRESH EVERY 1 MINUTE
TO user_daily_events_attributed
AS 
SELECT 
    uda.event_date,
    uda.event_id,
    ai.store_id,
    ai.network,
    ai.campaign_name,
    ai.campaign_id,
    ai.ad_name,
    ai.ad_id,
    ai.country_iso,
    ai.state_iso,
    ai.city_name,
    sum(uda.event_count) as event_count,
    count(distinct uda.oa_uid) as unique_users
FROM user_daily_events uda
LEFT JOIN attributed_installs ai ON uda.oa_uid = ai.oa_uid
GROUP BY 
    uda.event_date,
    uda.event_id,
    ai.store_id,
    ai.network,
    ai.campaign_name,
    ai.campaign_id,
    ai.ad_name,
    ai.ad_id,
    ai.country_iso,
    ai.state_iso,
    ai.city_name
;