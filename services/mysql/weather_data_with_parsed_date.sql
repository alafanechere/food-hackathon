CREATE VIEW weather_data_with_parsed_date AS
SELECT *, from_unixtime(date) AS parsed_date
FROM weather_data
