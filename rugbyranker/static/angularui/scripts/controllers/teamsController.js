sportModule.controller('teamsController', function ($scope, $http, $location, teamSearchService) {

    $http.get("/api/teams/")
        .then(function (response) {
            $scope.teams = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $scope.newpage = function(next){
        $http.get(next)
        .then(function (response) {
            $scope.teams = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });
    };

    $scope.clickteam = function(teamid){
        console.log($location.path("teams/"  + teamid))
    };

    $scope.search = function(){
            if ($scope.keywords.length >= 2){
            teamSearchService.search($scope.keywords).then(function(response){
                $scope.searchResponse = response.data;
                $scope.searchReponseLength = response.data.length;
                console.log($scope.searchResponse);
            });
            }
            else{
                $scope.searchResponse = null;
            }
        };


});