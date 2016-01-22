class ClustersController < ApplicationController
  layout :resolve_layout
  def home
    @request_types=Cluster.select("rtt","rtid").distinct
  end
  def index
    request_type=params[:rtid]
    @clusters=Cluster.where(:rtid=>request_type).order(score: :desc)
    @request_type=@clusters[0][:rtt]
  end
  def show
    @cluster=Cluster.find(params[:id_])
    @issues=Cluster.find(params[:id_]).issues
  end
  def resolve_layout
    case action_name
    when "show"
      "clusters_show_layout"
    else
      "clusters_layout"
    end
  end
end
