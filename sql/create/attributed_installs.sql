CREATE TABLE attributed_installs
(
    app_event_time DateTime64(3, 'UTC'),
    store_id LowCardinality(String),
    event_id LowCardinality(String),
    ifa UUID,
    client_ip String DEFAULT '',
    attribution_type LowCardinality(String),
    attribution_event_time DateTime64(3, 'UTC'),
    link_uid UUID,
    event_uid UUID,
    network LowCardinality(String) DEFAULT '',
    campaign_name LowCardinality(String) DEFAULT '',
    campaign_id LowCardinality(String) DEFAULT '',
    ad_name LowCardinality(String) DEFAULT '',
    ad_id LowCardinality(String) DEFAULT '',
    revenue Nullable(Decimal(9,4)) DEFAULT 0
) 
ENGINE = MergeTree 
PRIMARY KEY (store_id, ifa, client_ip)
ORDER BY (store_id, ifa, client_ip, event_id, app_event_time)
;
