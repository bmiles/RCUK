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

