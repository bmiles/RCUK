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

DROP VIEW IF EXISTS project_score;
CREATE VIEW project_score AS (
  SELECT po.ProjectId, 
    SUM(co.PrivateProbability) AS SumPrivateScore,
    COUNT(*) AS NumOrganisations
  FROM projectorganisations po
  LEFT JOIN classify_organisations co ON po.OrganisationId = co.OrganisationId
  GROUP BY po.ProjectId);

DROP TABLE IF EXISTS person_score;
CREATE TABLE person_score AS SELECT * FROM (
  SELECT peo.PersonId,
    COUNT(*) AS NumOrgs,
    SUM(co.PrivateProbability) AS NumPrivateOrgs
  FROM (
    SELECT DISTINCT pp.PersonId, pro.OrganisationId
      FROM projectperson pp
      INNER JOIN projectorganisations pro ON pp.ProjectId = pro.ProjectId) peo
    INNER JOIN classify_organisations co
      ON peo.OrganisationId = co.OrganisationId
    GROUP BY peo.PersonId
  ) ps1 NATURAL JOIN (
  SELECT pp.PersonId,
    COUNT(*) AS NumProjects,
    SUM(COALESCE(p.TotalGrantValue, p.ActualSpend)) AS TotalMoney,
    SUM(ps.SumPrivateScore * COALESCE(p.TotalGrantValue, p.ActualSpend)) /
      SUM(ps.NumOrganisations) AS PrivateMoney
  FROM projectperson pp 
  LEFT JOIN project p ON p.ProjectId = pp.ProjectId
  LEFT JOIN project_score ps ON ps.ProjectId = pp.ProjectId
  GROUP BY pp.PersonId) ps2;

