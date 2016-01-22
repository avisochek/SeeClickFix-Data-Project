class Issue < ActiveRecord::Base
  belongs_to :cluster, {:foreign_key=>'cluster_id'}



  Request_types=[
    "Bins for Trash & Recycling",
    "Graffiti",
    "Hangers",
    "Health Complaints",
    "Illegal Dumping",
    "Other",
    "Other - city responsibility",
    "Parking Violation/Abandoned Auto",
    "Parks Request",
    "Policing Issue",
    "Potholes",
    "Private Property Issue",
    "Public Space, Streets and Drains",
    "Sidewalks and Curb damage",
    "Signs / Bus Shelters / Pavement Markings",
    "Street Lamp",
    "Street Sweeping",
    "Traffic/Road Safety",
    "Traffic Signal / Pedestrian Signal",
    "Trash & Recycling",
    "Tree Trimming"
  ]
  Neighborhoods=[
    "Annex",
    "Beaver Hills",
    "Dixwell",
    "Downtown",
    "Dwight",
    "East Rock",
    "East Shore",
    "Edgewood",
    "Fair Haven",
    "Fair Haven Heights",
    "Hill",
    "Long Wharf",
    "Newhallville",
    "Prospect Hill",
    "Quinnipiac",
    "West River",
    "West Rock",
    "Westville",
    "Wooster Square/Mill River"
  ]

  def self.query_issues(parameters)
    issues=self.where(parameters)
    total_time,count,acknowledged,closed=0,0,0,0
    issues.each do |issue|
      if issue["acknowledged_at"]!=nil
        acknowledged+=1
        if issue["closed_at"]!=nil
          total_time+=(issue["created_at"]).to_i-(issue["closed_at"]).to_i
          closed+=1
        end
      end
      count+=1
    end

    if count >0
      avg_fix_time=(total_time.to_f/(count*1000*60*60*24)).round
      n_issues=count
      acknowledge_rate=acknowledged.to_f/count.to_f
      fix_rate = closed.to_f/acknowledged
      stat= {
            :n_issues=>n_issues,
            :acknowledge_rate=>acknowledge_rate,
            :fix_rate=>fix_rate,
            :avg_fix_time=>avg_fix_time
            }
    end
    return stat
  end

  def self.get_stats(param,days_back=nil,request_type=nil)
    stats=[]
    if param == :neighborhood
      Neighborhoods.each do |val|
        parameters= {param=>val}
        if not days_back==0
          parameters[:created_at] = (Time.now.midnight - days_back.day)..Time.now.midnight
        end
        stat=query_issues(parameters)
        if stat
          stat[param]=val
          stats.push stat
        end
      end
    elsif param == :rtt
      Request_types.each do |val|
        parameters= {param=>val}
        if not days_back==0
          parameters[:created_at] = (Time.now.midnight - days_back.day)..Time.now.midnight
        end
        stat=query_issues(parameters)
        if stat
          stat[param]=val
          stats.push stat
        end
      end
    elsif param == :both
      Neighborhoods.each do |val|
        parameters= {:neighborhood=>val,:rtt=>request_type}
        if not days_back==0
          parameters[:created_at] = (Time.now.midnight - days_back.day)..Time.now.midnight
        end
        stat=query_issues(parameters)
        if stat
          stat[:neighborhood]=val
          stats.push stat
        end
      end
    end
    return stats
  end
end
