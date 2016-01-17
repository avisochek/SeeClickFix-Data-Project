class Cluster < ActiveRecord::Base
  has_many :issues ,{:primary_key => 'id_'}
  self.primary_key = 'id_'
end
