require 'test_helper'

class IssuesControllerTest < ActionController::TestCase
  setup do
    @issue = issues(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:issues)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create issue" do
    assert_difference('Issue.count') do
      post :create, issue: { acknowledged: @issue.acknowledged, adress: @issue.adress, created_at: @issue.created_at, id_: @issue.id_, integer: @issue.integer, lat: @issue.lat, lng: @issue.lng, neighborhood: @issue.neighborhood, rtid: @issue.rtid, rtt: @issue.rtt, status: @issue.status, street_name: @issue.street_name }
    end

    assert_redirected_to issue_path(assigns(:issue))
  end

  test "should show issue" do
    get :show, id: @issue
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @issue
    assert_response :success
  end

  test "should update issue" do
    patch :update, id: @issue, issue: { acknowledged: @issue.acknowledged, adress: @issue.adress, created_at: @issue.created_at, id_: @issue.id_, integer: @issue.integer, lat: @issue.lat, lng: @issue.lng, neighborhood: @issue.neighborhood, rtid: @issue.rtid, rtt: @issue.rtt, status: @issue.status, street_name: @issue.street_name }
    assert_redirected_to issue_path(assigns(:issue))
  end

  test "should destroy issue" do
    assert_difference('Issue.count', -1) do
      delete :destroy, id: @issue
    end

    assert_redirected_to issues_path
  end
end
