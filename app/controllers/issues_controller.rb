require "time"

class IssuesController < ApplicationController

  def home
  end

  def stats_by_neighborhood
    @stats=Issue.get_stats(:neighborhood,params[:days_back].to_i)
  end

  def stats_by_request_type
    @stats=Issue.get_stats(:rtt,params[:days_back].to_i)
  end

  def stats_by_request_type_and_neighborhood
    @request_type=params[:request_type]
    @stats=Issue.get_stats(:both,params[:days_back].to_i,request_type=params[:request_type])
  end
end
