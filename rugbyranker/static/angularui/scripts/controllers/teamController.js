sportModule.controller('teamController', function ($scope, $http, $routeParams, $location) {

    var teamId = String($routeParams.teamId);


    $http.get("/api/teams/" + teamId + '/details/')
        .then(function (response) {
            $scope.details = response.data;

            //For Streak Chart
            $scope.streakLabels = ['Max Streak', 'Current Streak'];
            $scope.streakSeries = [];
            $scope.streakData = [[response.data.max_streak], [response.data.current_streak]];

            //For Current Position Arrows
            var thisweek = response.data.thisweek_position;
            var lastweek = response.data.lastweek_position;

            if (thisweek == lastweek){
                $scope.changesame = true;
            }
            else if (thisweek < lastweek){
                $scope.changeup = true;
            }
            else{
                $scope.changedown = true;
            }


            console.log("Http Sucess");
            console.log(response.data);
        }, function errorCallback(response) {
            console.log(response);
            $location.url('/error');
        });

    $http.get("/api/teams/" + teamId + '/matches/')
        .then(function (response) {
            $scope.teammatchdata = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/teams/" + teamId + '/information/')
        .then(function (response) {
            $scope.information = response.data;

            var homeCtx = document.getElementById("homeCtxChart");
            var awayCtx = document.getElementById("awayCtxChart");

            var homeData = {
                labels: [
                    "Wins",
                    "Losses",
                    "Draws"
                ],
                datasets: [
                    {
                        data: [response.data.won_home, response.data.lost_home, response.data.drew_home],
                        backgroundColor: [
                            "#36A2EB",
                            "#FF6384",
                            "#FFCE56"
                        ],
                        hoverBackgroundColor: [
                            "#36A2EB",
                            "#FF6384",
                            "#FFCE56"
                        ]
                    }]
            };

            var awayData = {
                labels: [
                    "Wins",
                    "Losses",
                    "Draws"
                ],
                datasets: [
                    {
                        data: [response.data.won_away, response.data.lost_away, response.data.drew_away],
                        backgroundColor: [
                            "#36A2EB",
                            "#FF6384",
                            "#FFCE56"
                        ],
                        hoverBackgroundColor: [
                            "#36A2EB",
                            "#FF6384",
                            "#FFCE56"
                        ]
                    }]
            };

            var homeCtxChart = new Chart(homeCtx, {
                type: 'doughnut',
                data: homeData
            });

            var awayCtxChart = new Chart(awayCtx, {
                type: 'doughnut',
                data: awayData
            });
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

    $scope.sortType = 'position';
    $scope.sortReverse = false;
    $scope.searchRivals = '';

    $scope.clickteam = function (teamid) {
        console.log($location.path("teams/" + teamid))
    };


    //GRAPH CONTROLLER
    $http.get("/api/teams/" + teamId + '/rankhistory/')
        .then(function (response) {
            rankhistory = response.data;
            dates = [];
            ratings = [];
            rankhistory = JSON.parse(rankhistory);
            rankhistory.forEach(function (arrayItem) {
                if (arrayItem.rating > 5){
                    var rating = arrayItem.rating;
                    var date = arrayItem.date;
                    dates.push(date);
                    ratings.push(rating);
                }
            });

            var options = {
                fill: true
            };

            var data = {
                labels: dates,
                datasets: [
                    {
                        label: "Ranking",
                        lineTension: 0.1,
                        backgroundColor: "rgba(2, 22, 40, 0.6)",
                        borderColor: "rgba(2, 22, 40, 1)",
                        borderCapStyle: 'butt',
                        borderDash: [],
                        borderDashOffset: 0.0,
                        borderJoinStyle: 'miter',
                        pointBorderColor: "rgba(2, 22, 40, 1)",
                        pointBackgroundColor: "#fff",
                        pointBorderWidth: 1,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: "rgba(2, 22, 40, 1)",
                        pointHoverBorderColor: "rgba(2, 22, 40, 1)",
                        pointHoverBorderWidth: 2,
                        pointRadius: 1,
                        pointHitRadius: 10,
                        data: ratings,
                        spanGaps: false,
                        fill: true,
                        cubicInterpolationMode: 'default'
                    }
                ]
            };
            var rankingHistoryCtx = document.getElementById("myLineChart");
            var myLineChart = new Chart(rankingHistoryCtx, {
                type: 'line',
                data: data,
                options: options
            });

            console.log("Http Sucess");
        });

});

