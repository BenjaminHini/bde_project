CREATE EXTERNAL TABLE ece_2022_fall_bda_1.${hiveUsername}_bde_project_db_ext (
dates string,
signs int,
description string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
TBLPROPERTIES ('skip.header.line.count'='1');

LOAD DATA INPATH '/user/${clusterUsername}/oozie_wf/db/daily_scrap.json' INTO TABLE ece_2022_fall_bda_1.${hiveUsername}_bde_project_db_ext;

INSERT INTO TABLE ece_2022_fall_bda_1.${hiveUsername}_bde_project_db SELECT * FROM ece_2022_fall_bda_1.${hiveUsername}_bde_project_db_ext;

DROP TABLE ece_2022_fall_bda_1.${hiveUsername}_bde_project_db_ext;