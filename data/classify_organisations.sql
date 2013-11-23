DROP TABLE IF EXISTS classify_organisations;

CREATE TABLE classify_organisations (
  OrganisationId VARCHAR(128) PRIMARY KEY,
  PrivateProbability DOUBLE
);

LOAD DATA LOCAL INFILE 'classify_organisations.csv' REPLACE
INTO TABLE classify_organisations 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

DROP VIEW IF EXISTS project_private_score;

CREATE VIEW project_private_score AS (
  SELECT po.ProjectId, SUM(co.PrivateProbability) AS PrivateScore
  FROM projectorganisations po
  LEFT JOIN classify_organisations co ON po.OrganisationId = co.OrganisationId
  GROUP BY po.ProjectId);

