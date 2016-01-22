class Issue < ActiveRecord::Base
  belongs_to :cluster, {:foreign_key=>'cluster_id'}
end
