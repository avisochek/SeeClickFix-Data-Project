# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)
require 'csv'

CSV.foreach('data/nh_issues_data.csv') do |status,neighborhood,street_name,rtid,rtt,address,lat,lng,id_,created_at,acknowledged|
  Issue.create(status:status,neighborhood:neighborhood,street_name:street_name,rtid:rtid,rtt:rtt,adress:address,lat:lat,lng:lng,id_:id_,created_at:created_at,acknowledged:acknowledged)
end
