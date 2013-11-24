#
# Build a hash of projects to people
#
require './common'

pp = $db.query(<<SQL)
SELECT ProjectId, PersonId FROM projectperson
ORDER BY ProjectId, PersonId
SQL

File.open('person_projects.json', 'wb') do |f|
  f.puts JSON.dump(Hash[pp.
    group_by {|x| x['ProjectId'].upcase}.
    map {|projectId, records|
      [projectId, records.map {|record| record['PersonId']}]}])
end
