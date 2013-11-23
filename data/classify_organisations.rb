#
# Steps:
#   irb
#   > require './classify_organisations.rb'
#   > make_training_set(100)
#   # manually classify them...
#   > data_to_csv 'organisations.csv', $ou
#
#   Then run the classify_organisations.py script, which produces
#   classify_organisations.csv.
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
# Print to CSV.
#
def data_to_csv file_name, rows
  CSV.open(file_name, 'wb') do |csv|
    csv << rows.first.keys.to_a
    rows.each do |row|
      csv << row.values.to_a
    end
  end
  nil
end

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
