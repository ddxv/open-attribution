CREATE MATERIALIZED VIEW attribute_installs_mv
REFRESH EVERY 1 MINUTE
TO attributed_installs
AS
SELECT * FROM attributed_clicks
UNION ALL
SELECT * FROM attributed_impressions
;
