--
-- Setup:
-- create database gtr_repo;
-- create user 'rcuk'@'localhost' identified by 'rcuk1234';
-- grant all privileges on *.* to 'rcuk'@'localhost' with grant option;
--
-- Import:
-- mysql --user=rcuk --password=rcuk1234 gtr_repo <gtr_repo*.sql
-- mysql --user=rcuk --password=rcuk1234 gtr_repo <person_org*.sql
--

--
-- Find all of the organisations that each person has worked with
-- on a project.
--
DROP VIEW IF EXISTS person_organisation_partners;
CREATE VIEW person_organisation_partners AS (
  SELECT po.ProjectId, po.OrganisationId, pp.PersonId,
    p.FirstName, p.SecondName, p.Surname,
    pr.ProjectTitle,
    o.Name AS OrganisationName,
    o.OrganisationUnitType,
    o.Website AS OrganisationWebsite,
    o.CHRegistrationNumber AS OrganisationRegistrationNumber
  FROM projectorganisations po
  LEFT JOIN projectperson pp ON po.ProjectId = pp.ProjectId
  LEFT JOIN project pr ON pr.ProjectID = pp.ProjectId
  LEFT JOIN person p ON p.PersonId = pp.PersonId
  LEFT JOIN organisationunit o ON o.OrganisationId = po.OrganisationId
);

