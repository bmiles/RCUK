require 'bundler/setup'
Bundler.require(:default)

require 'csv'

# for Marius's laptop:
#$db = Mysql2::Client.new(
#  :host => "172.16.97.5",
#  :username => "rcuk",
#  :password => "rcuk1234",
#  :database => "gtr_repo")

# for local install
$db = Mysql2::Client.new(
  :username => "rcuk",
  :password => "rcuk1234",
  :database => "gtr_repo")

#
# Print rows in MySql2 query hash format to CSV.
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


