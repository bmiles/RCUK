require './common'

table = ARGV.shift
raise "no table name given" unless table

file_name = ARGV.shift
raise "no file name given" unless file_name

data_to_csv file_name, $db.query("SELECT * FROM #{table}")
