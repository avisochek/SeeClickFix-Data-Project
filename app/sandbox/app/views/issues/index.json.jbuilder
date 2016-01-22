json.array!(@issues) do |issue|
  json.extract! issue, :id, :status, :created_at, :neighborhood, :street_name, :acknowledged, :rtid, :rtt, :adress, :lat, :lng, :id_, :integer
  json.url issue_url(issue, format: :json)
end
