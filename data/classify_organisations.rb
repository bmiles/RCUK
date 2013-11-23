#
# Steps:
#   irb
#   > require './classify_organisations.rb'
#   > make_training_set(100)
#   # manually classify them...
#   > data_to_csv 'organisations.csv', $ou
#
#   Then run the classify_organisations.py script, which produces
#   classify_organisations.csv. It's not very big, so I've checked the latest
#   version into source control.
#
#   Then run the classify_organisations.sql script to load the resulting
#   classification into the database and create the project_private_score view.
#
#   Then export it with
#   ruby dump_to_csv.rb project_private_score project_private_score.csv
#
# Notes:
#
# The GtR guys said that the 'parent' OU stuff is mostly blank (not yet
# implemented).
#
# The 'D' for OrganisationUnitType means 'department'
#

require './common'

$ou = $db.query(<<SQL)
SELECT OrganisationId,
  Name,
  OrganisationUnitType = 'D' AS Department,
  NOT CHRegistrationNumber IS NULL AS Registered
  FROM organisationunit
SQL

#
# Select some random organisations for manual classification.
#
def make_training_set training_set_size
  sample = $ou.to_a.sample(training_set_size).shuffle
  data_to_csv 'train.csv', sample
end

# positive indicators:
#   limited
#   ltd
#   plc
#   c.i.c. (community interest company)
#   alliance
#   llc
#
# negative indicators:
#   school
#   university
#   center
#   centre
#   
