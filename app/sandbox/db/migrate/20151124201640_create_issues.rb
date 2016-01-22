class CreateIssues < ActiveRecord::Migration
  def change
    create_table :issues do |t|
      t.string :status
      t.string :created_at
      t.string :neighborhood
      t.string :street_name
      t.boolean :acknowledged
      t.string :rtid
      t.string :rtt
      t.string :adress
      t.float :lat
      t.float :lng
      t.string :id_
      t.string :integer

      t.timestamps null: false
    end
  end
end
