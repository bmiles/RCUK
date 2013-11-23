DROP VIEW IF EXISTS person_organisation_partners;

--
-- Find all of the organisations that each person has worked with
-- on a project.
--
CREATE VIEW person_organisation_partners AS (
  SELECT po.ProjectId, po.OrganisationId, pp.PersonId,
    p.FirstName, p.SecondName, p.Surname,
    pr.ProjectTitle,
    o.Name, o.OrganisationUnitType, o.Website, o.CHRegistrationNumber
  FROM projectorganisations po
  LEFT JOIN projectperson pp ON po.ProjectId = pp.ProjectId
  LEFT JOIN project pr ON pr.ProjectID = pp.ProjectId
  LEFT JOIN person p ON p.PersonId = pp.PersonId
  LEFT JOIN organisationunit o ON o.OrganisationId = po.OrganisationId
);
