Rails.application.routes.draw do
  get '/' => 'issues#home'
  post '/issues/stats_by_neighborhood' => 'issues#stats_by_neighborhood'
  post '/issues/stats_by_request_type' => 'issues#stats_by_request_type'
  post '/issues/stats_by_request_type_and_neighborhood' => 'issues#stats_by_request_type_and_neighborhood'

  get '/clusters' => 'clusters#home'
  get '/clusters/index/:rtid' => 'clusters#index'
  get '/clusters/:id_' => 'clusters#show', as: 'cluster'

  ### redirect home when user refreshes the page
  get '/issues/stats_by_neighborhood' => 'issues#home'
  get '/issues/stats_by_request_type' => 'issues#home'
  get '/issues/stats_by_request_type_and_neighborhood' => 'issues#home'

  get'/clusters/show' => 'clusters#home'


  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  # root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end
