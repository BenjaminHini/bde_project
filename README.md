# ece-bigdata-2022-fall project

## Git
- git clone https://github.com/BenjaminHini/bde_project/ (it will require a personnal access token to clone it in the adaltas ssh)

- hdfs dfs -copyFromLocal /bde_project /path (here, our path is /education/ece_2022_fall_bda_1/b.hini-ece/project)

## Data Scrapping

All our data is scrapped in python from the website 'https://www.horoscope.com/'.
The python script needs 2 hours to be fully executed, so we give the csv file in db/data.csv

## Storing the data

Now that the data is generated from the python script, we load the csv file into an external database, and into an ORC database.

We first set our clusterUsername and hiveUsername :

```
SET hivevar:clusterUsername = p.nom-ece;
SET hivevar:hiveUsername=p_nom_ece; 
```

Then, we create our external table with the 3 columns dates, signs and description in the location of our data.csv (in the folder db)

```
CREATE EXTERNAL TABLE ece_2022_fall_bda_1.${hiveUsername}_bde_project_db_ext (
dates string,
signs int,
description string)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS TEXTFILE
LOCATION '/path/bde_project/db'
TBLPROPERTIES ('skip.header.line.count'='1');
```

We check if the data is well stored : 
```
select * from ece_2022_fall_bda_1.${hiveUsername}_bde_project_db_ext limit 5;
```

It should print something like this : 

![Ext db](img/ext_db.jpg)


Now, we can create the ORC table : 

```
CREATE TABLE ece_2022_fall_bda_1.${hiveUsername}_bde_project_db (
dates string,
signs int,
description string)
STORED AS ORC;
```

We just have to insert all the data from the external table to the ORC table :
```
INSERT INTO TABLE ece_2022_fall_bda_1.${hiveUsername}_bde_project_db SELECT * FROM ece_2022_fall_bda_1.${hiveUsername}_bde_project_db_ext;
```

We check if the data is well stored in the ORC table: 
```
select * from ece_2022_fall_bda_1.${hiveUsername}_bde_project_db limit 5;
```

It should print something like this : 

![ORC db](img/orc_db.jpg)



**Contact**: 
- alexandre.abadie@edu.ece.fr
- benjamin.hini@edu.ece.fr
- romain.ribeiro@edu.ece.fr
- yann.messalati@edu.ece.fr
