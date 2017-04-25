sportModule.controller('teamController', function ($scope, $http, $routeParams, $location) {

    var teamId = String($routeParams.teamId);


    $http.get("/api/teams/" + teamId + '/details/')
        .then(function (response) {
            $scope.details = response.data;

            //For Streak Chart
            $scope.streakLabels = ['Max Streak', 'Current Streak'];
            $scope.streakSeries = [];
            $scope.streakData = [[response.data.max_streak], [response.data.current_streak]];

            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/matches/home/')
        .then(function (response) {
            $scope.homematchdata = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/matches/away/')
        .then(function (response) {
            $scope.awaymatchdata = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/information/')
        .then(function (response) {
            $scope.information = response.data;

            //For Home Chart
            $scope.homeMatchLabels = ["Home Wins", "Home Losses", "Home Draws"];
            $scope.homeMatchData = [response.data.won_home, response.data.lost_home, response.data.drew_home];

            //For Away Chart
            $scope.awayMatchLabels = ["Away Wins", "Away Losses", "Away Draws"];
            $scope.awayMatchData = [response.data.won_away, response.data.lost_away, response.data.drew_away];

            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/rivals/')
        .then(function (response) {
            $scope.rivals = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/history/')
        .then(function (response) {
            $scope.history = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/currentranking/')
        .then(function (response) {
            $scope.currentranking = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $scope.sortType     = 'position';
    $scope.sortReverse  = false;
    $scope.searchRivals   = '';

    $scope.clickteam = function(teamid){
        console.log($location.path("teams/"  + teamid))
    };

});

