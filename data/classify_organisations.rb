require './common'

#
# Notes:
#
# The GtR guys said that the 'parent' OU stuff is mostly blank (not yet
# implemented).
#
# The 'D' for OrganisationUnitType means 'department'
#

$ou = $db.query(<<SQL)
SELECT OrganisationId,
  Name,
  OrganisationUnitType = 'D' AS Department,
  NOT CHRegistrationNumber IS NULL AS Registered
  FROM organisationunit
SQL

def make_training_data training_set_size
  sample = $ou.to_a.sample(training_set_size).shuffle
  CSV.open('train.csv', 'wb') do |csv|
    csv << sample.first.keys.to_a
    sample.each do |row|
      csv << row.values.to_a
    end
  end
  nil
end
#make_training_data(100)

puts ou.select {|x| x['Registered'] != 0}.map {|x| x['Name']}

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
