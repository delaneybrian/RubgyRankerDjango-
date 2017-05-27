sportModule.controller('comparisonController', function ($scope, $http, $location, teamSearchService) {

    $scope.searchA = function () {
        if ($scope.keywordsA.length >= 2) {
            teamSearchService.search($scope.keywordsA).then(function (response) {
                $scope.searchResponseA = response.data;
                $scope.searchReponseLengthA = response.data.length;
            });
        }
        else {
            $scope.searchResponseA = null;
        }
    };

    $scope.selectedTeams = [];

    $scope.addTeam = function (team) {
        $scope.errorMessage = null;
        $scope.showSearchWarning = false;

        var included = $scope.selectedTeams.indexOf(team);

        if ($scope.selectedTeams.length >= 2) {
            $scope.errorMessage = "Cannot Compare More Than Two Teams";
            $scope.showSearchWarning = true;
        }
        else if (included != -1) {
            $scope.errorMessage = "Cannot Compare A Team Against Itself"
        }
        else {
            $scope.keywordsA = "";
            $scope.searchResponseA = null;
            $scope.selectedTeams.push(team);
        }
    };

    $scope.removeTeam = function (team) {
        $scope.errorMessage = null;
        var index = $scope.selectedTeams.indexOf(team);
        $scope.selectedTeams.splice(index, 1);
    };

    $scope.compareTeams = function () {
        $scope.errorMessage = null;
        $scope.showSearchWarning = false;


        if ($scope.selectedTeams.length == 2) {
            teamA = $scope.selectedTeams[0];
            teamB = $scope.selectedTeams[1];
            console.log($location.path("comparison/teamA/" + teamA.id + "/teamB/" + teamB.id + "/"))

        }
        else {
            $scope.errorMessage = "Need At Least Two Teams To Compare"
            $scope.showSearchWarning = true;
        }
    }

});

sportModule.controller('comparisonSelectionController', function ($scope, $routeParams, $location, $http) {

    var teamAId = String($routeParams.teamAId);
    var teamBId = String($routeParams.teamBId);

    $http.get("/api/comparison/?teamA=" + teamAId + '&teamB=' + teamBId)

        .then(function (response) {
            $scope.teamDetails = response.data;
            console.log(response.data);
            $scope.teamAName = $scope.teamDetails.teamAData.name;
            $scope.teamBName = $scope.teamDetails.teamBData.name;


            if($scope.teamDetails.recentMatches.length == 0){
                $scope.DoNotDisplayMatches = true;
            }

            if($scope.teamDetails.headToHeadForm.length == 0){
                $scope.DoNotDisplayForm = true;
            }

            //For Current Position Arrows
            var thisweekA = $scope.teamDetails.teamAData.thisweek_position;
            var lastweekA = $scope.teamDetails.teamAData.lastweek_position;


            if (thisweekA == lastweekA){
                $scope.changesameA = true;
            }
            else if (thisweekA < lastweekA){
                $scope.changeupA = true;
            }
            else{
                $scope.changedownA = true;
            }

            var thisweekB = $scope.teamDetails.teamBData.thisweek_position;
            var lastweekB = $scope.teamDetails.teamBData.lastweek_position;


            if (thisweekB == lastweekB){
                $scope.changesameB = true;
            }
            else if (thisweekB < lastweekB){
                $scope.changeupB = true;
            }
            else{
                $scope.changedownB = true;
            }


            /* COMPARISON HISTORIC SCORING CHART */
            var teamArate = ($scope.teamDetails.normailizedHistoricRatings.normalizedTeamARankings);
            var teamBrate = ($scope.teamDetails.normailizedHistoricRatings.normalizedTeamBRankings);
            var dates = ($scope.teamDetails.normailizedHistoricRatings.normalizedDates);

            var data = {
                labels: dates,
                datasets: [
                    {
                        label: $scope.teamAName,
                        lineTension: 0.1,
                        backgroundColor: "rgba(255, 65, 54, 0.6)",
                        borderColor: "rgba(255, 65, 54, 1)",
                        borderCapStyle: 'butt',
                        borderDash: [],
                        borderDashOffset: 0.0,
                        borderJoinStyle: 'miter',
                        pointBorderColor: "rgba(255, 65, 54, 1)",
                        pointBackgroundColor: "#fff",
                        pointBorderWidth: 1,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: "rgba(255, 65, 54, 1)",
                        pointHoverBorderColor: "rgba(255, 65, 54, 1)",
                        pointHoverBorderWidth: 2,
                        pointRadius: 1,
                        pointHitRadius: 10,
                        data: teamArate,
                        spanGaps: false,
                        fill: false,
                        cubicInterpolationMode: 'default'
                    },
                    {
                        label: $scope.teamBName,
                        lineTension: 0.1,
                        backgroundColor: "rgba(0, 116, 217, 0.6)",
                        borderColor: "rgba(0, 116, 217, 1)",
                        borderCapStyle: 'butt',
                        borderDash: [],
                        borderDashOffset: 0.0,
                        borderJoinStyle: 'miter',
                        pointBorderColor: "rgba(0, 116, 217, 1)",
                        pointBackgroundColor: "rgba(76,0,0)",
                        pointBorderWidth: 1,
                        pointHoverRadius: 5,
                        pointHoverBackgroundColor: "rgba(0, 116, 217, 1)",
                        pointHoverBorderColor: "rgba(0, 116, 217, 1)",
                        pointHoverBorderWidth: 2,
                        pointRadius: 1,
                        pointHitRadius: 10,
                        data: teamBrate,
                        spanGaps: false,
                        fill: false,
                        cubicInterpolationMode: 'default'
                    }
                ]
            };

            var options = { };
            var rankingHistoryCtx = document.getElementById("myLineChart");
            var myLineChart = new Chart(rankingHistoryCtx, {
                type: 'line',
                data: data,
                options: options
            });


            /* GENERAL COMPARISON SCORING RATE BAR CHART */

            var teamAAllAverageScore = ($scope.teamDetails.allGamesAverage.teamAAllAverageScore);
            var teamBAllAverageScore = ($scope.teamDetails.allGamesAverage.teamBAllAverageScore);
            var teamAAllAverageHomeScore = ($scope.teamDetails.allGamesAverage.teamAAllAverageHomeScore);
            var teamBAllAverageHomeScore = ($scope.teamDetails.allGamesAverage.teamBAllAverageHomeScore);
            var teamAAllAverageAwayScore = ($scope.teamDetails.allGamesAverage.teamAAllAverageAwayScore);
            var teamBAllAverageAwayScore = ($scope.teamDetails.allGamesAverage.teamBAllAverageAwayScore);



            var scoringRateData = {
                labels: [
                            "Average Score", "Average Score",
                            "Average Home Score", " Average Home Score",
                            "Average Away Score", "Average Away Score"
                ],
                datasets: [
                    {
                        label: "Scoring Rate Comparison",
                        backgroundColor: [
                            'rgba(2, 22, 40, 1)',
                            'rgba(165, 183, 202, 1)',
                            'rgba(2, 22, 40, 1)',
                            'rgba(165, 183, 202, 1)',
                            'rgba(2, 22, 40, 1)',
                            'rgba(165, 183, 202, 1)'
                        ],
                        borderColor: [
                            'rgba(2, 22, 40, 0.2)',
                            'rgba(165, 183, 202, 0.2)',
                            'rgba(2, 22, 40, 0.2)',
                            'rgba(165, 183, 202, 0.2)',
                            'rgba(2, 22, 40, 0.2)',
                            'rgba(165, 183, 202, 0.2)'
                        ],
                        borderWidth: 1,
                        data: [teamAAllAverageScore, teamBAllAverageScore, teamAAllAverageHomeScore,
                            teamBAllAverageHomeScore, teamAAllAverageAwayScore, teamBAllAverageAwayScore]
                    }
                ]
            };

            var options = { legend: { display: false }};

            var scoringRateCtx = document.getElementById("myScoringRateChart");
            var myScoringRateChart = new Chart(scoringRateCtx, {
                type: 'bar',
                data: scoringRateData,
                options: options
            });


            /* HEAD TO HEAD COMPARISON SCORING RATE BAR CHART */

            if($scope.teamDetails.vsScoresDict == 0){
                $scope.displayVsScoringRates = false;
            }
            else {
                $scope.displayVsScoringRates = true;
            }
                var teamAAverageScore = ($scope.teamDetails.vsScoresDict.teamAAvreageScore);
                var teamBAverageScore = ($scope.teamDetails.vsScoresDict.teamBAvreageScore);
                var teamAAverageHomeScore = ($scope.teamDetails.vsScoresDict.teamAAverageHomeScore);
                var teamBAverageHomeScore = ($scope.teamDetails.vsScoresDict.teamBAverageHomeScore);
                var teamAAverageAwayScore = ($scope.teamDetails.vsScoresDict.teamAAverageAwayScore);
                var teamBAverageAwayScore = ($scope.teamDetails.vsScoresDict.teamBAverageAwayScore);

                var scoringH2HRateData = {
                    labels: [
                        "Average Score", "Average Score",
                        "Average Home Score", "Average Home Score",
                        "Average Away Score", "Average Away Score"
                    ],
                    datasets: [
                        {
                            label: "Scoring Rate Comparison",
                            backgroundColor: [
                                'rgba(2, 22, 40, 1)',
                                'rgba(165, 183, 202, 1)',
                                'rgba(2, 22, 40, 1)',
                                'rgba(165, 183, 202, 1)',
                                'rgba(2, 22, 40, 1)',
                                'rgba(165, 183, 202, 1)'
                            ],
                            borderColor: [
                                'rgba(2, 22, 40, 0.2)',
                                'rgba(165, 183, 202, 0.2)',
                                'rgba(2, 22, 40, 0.2)',
                                'rgba(165, 183, 202, 0.2)',
                                'rgba(2, 22, 40, 0.2)',
                                'rgba(165, 183, 202, 0.2)'
                            ],
                            borderWidth: 1,
                            data: [teamAAverageScore, teamBAverageScore, teamAAverageHomeScore,
                                teamBAverageHomeScore, teamAAverageAwayScore, teamBAverageAwayScore]
                        }
                    ]
                };
                var options = {legend: {display: false}};

                var scoringRateH2HCtx = document.getElementById("myHtoHScoringRateChart");
                var myHtoHScoringRateChart = new Chart(scoringRateH2HCtx, {
                    type: 'bar',
                    data: scoringH2HRateData,
                    options: options
                });

            /* STREAK COMPARISON CHARTS */

            if($scope.teamDetails.vsScoresDict == 0){
                $scope.displayVsScoringRates = false;
            }
            else {
                $scope.displayVsScoringRates = true;
            }
            /* HEAD TO HEAD */
            var teamACurrentStreakHtH = ($scope.teamDetails.streakAndWins.teamACurrentStreak);
            var teamBCurrentStreakHtH = ($scope.teamDetails.streakAndWins.teamBCurrentStreak);
            var teamAMaxStreakH2H = ($scope.teamDetails.streakAndWins.teamAMaxStreak);
            var teamBMaxStreakHtH = ($scope.teamDetails.streakAndWins.teamBMaxStreak);



            var streakH2HData = {
                labels: [
                            "Current Streak",
                            "Current Streak",
                            "Max Streak",
                            "Max Streak"
                ],
                datasets: [
                    {
                        label: null,
                        backgroundColor: [
                            'rgba(2, 22, 40, 1)',
                            'rgba(165, 183, 202, 1)',
                            'rgba(2, 22, 40, 1)',
                            'rgba(165, 183, 202, 1)',
                            'rgba(2, 22, 40, 1)',
                            'rgba(165, 183, 202, 1)'
                        ],
                        borderColor: [
                            'rgba(2, 22, 40, 0.2)',
                            'rgba(165, 183, 202, 0.2)',
                            'rgba(2, 22, 40, 0.2)',
                            'rgba(165, 183, 202, 0.2)',
                            'rgba(2, 22, 40, 0.2)',
                            'rgba(165, 183, 202, 0.2)'
                        ],
                        borderWidth: 1,
                        data: [teamACurrentStreakHtH, teamBCurrentStreakHtH,
                            teamAMaxStreakH2H, teamBMaxStreakHtH]
                    }
                ]
            };

            var options = { legend: { display: false }};

            var streakH2HCtx = document.getElementById("headToHeadStreakChart");
            var headToHeadStreakChart = new Chart(streakH2HCtx, {
                type: 'horizontalBar',
                data: streakH2HData,
                options: options
            });


            /* GENERAL */
            var teamACurrentStreakGen = ($scope.teamDetails.teamAData.current_streak);
            var teamBCurrentStreakGen = ($scope.teamDetails.teamBData.current_streak);
            var teamAMaxStreakGen = ($scope.teamDetails.teamAData.max_streak);
            var teamBMaxStreakGen = ($scope.teamDetails.teamBData.max_streak);

            var streakGenData = {
                labels: [
                            "Current Streak",
                            "Current Streak",
                            "Max Streak",
                            "Max Streak"
                ],
                datasets: [
                    {
                        label: false,
                        backgroundColor: [
                            'rgba(2, 22, 40, 1)',
                            'rgba(165, 183, 202, 1)',
                            'rgba(2, 22, 40, 1)',
                            'rgba(165, 183, 202, 1)',
                            'rgba(2, 22, 40, 1)',
                            'rgba(165, 183, 202, 1)'
                        ],
                        borderColor: [
                            'rgba(2, 22, 40, 0.2)',
                            'rgba(165, 183, 202, 0.2)',
                            'rgba(2, 22, 40, 0.2)',
                            'rgba(165, 183, 202, 0.2)',
                            'rgba(2, 22, 40, 0.2)',
                            'rgba(165, 183, 202, 0.2)'
                        ],
                        borderWidth: 1,
                        data: [teamACurrentStreakGen, teamBCurrentStreakGen,
                            teamAMaxStreakGen, teamBMaxStreakGen]
                    }
                ]
            };

            var options = { legend: { display: false }};

            var streakGenCtx = document.getElementById("generalStreakChart");
            var generalStreakChart = new Chart(streakGenCtx, {
                type: 'horizontalBar',
                data: streakGenData,
                options: options
            });



        }, function errorCallback(response) {
            $location.url('/error');
        });




    $http.get("/api/teams/"+ teamAId + "/information/")
        .then(function (response) {
            var homeMatches = response.data.home_matches;
            var awayMatches = response.data.away_matches;
            var totalMatches = homeMatches + awayMatches;
            var wonAwayMatches = response.data.won_away;
            var lostAwayMatches = response.data.lost_away;
            var drewAwayMatches = response.data.drew_home;
            var wonHomeMatches = response.data.won_home;
            var lostHomeMatches = response.data.lost_home;
            var drewHomeMatches = response.data.drew_home;
            var wonMatches = wonHomeMatches + wonAwayMatches;
            var lostMatches = lostHomeMatches + lostAwayMatches;
            var drewMatches = drewHomeMatches + drewAwayMatches;

            $scope.teamAHomeWinPrecentage = (wonHomeMatches/homeMatches)*100;
            $scope.teamAAwayWinPrecentage = (wonAwayMatches/awayMatches)*100;
            $scope.teamAWinPrecentage = (wonMatches/totalMatches)*100;

            var teamAWinData = {
                labels: [
                    "Wins: " + wonMatches,
                    "Losses: " + lostMatches,
                    "Draws: " + drewMatches
                ],
                datasets: [
                    {
                        data: [wonMatches, lostMatches, drewMatches],
                        backgroundColor: [
                            "rgba(2, 22, 40, 1)",
                            "#A5B7CA",
                            "#FFCE56"
                        ],
                        hoverBackgroundColor: [
                            "rgba(2, 22, 40, 1)",
                            "#A5B7CA",
                            "#FFCE56"
                        ]
                    }]
            };

            var options = { tooltips: {enabled: false }};
            var teamAWinsCtx = document.getElementById("teamAWinsTable");
            var teamAWinsTable = new Chart(teamAWinsCtx, {
                type: 'pie',
                data: teamAWinData,
                options: options
            });
        });

    $http.get("/api/teams/"+ teamBId + "/information/")
        .then(function (response) {
            var homeMatches = response.data.home_matches;
            var awayMatches = response.data.away_matches;
            var totalMatches = homeMatches + awayMatches;
            var wonAwayMatches = response.data.won_away;
            var lostAwayMatches = response.data.lost_away;
            var drewAwayMatches = response.data.drew_home;
            var wonHomeMatches = response.data.won_home;
            var lostHomeMatches = response.data.lost_home;
            var drewHomeMatches = response.data.drew_home;
            var wonMatches = wonHomeMatches + wonAwayMatches;
            var lostMatches = lostHomeMatches + lostAwayMatches;
            var drewMatches = drewHomeMatches + drewAwayMatches;

            $scope.teamBHomeWinPrecentage = (wonHomeMatches/homeMatches)*100;
            $scope.teamBAwayWinPrecentage = (wonAwayMatches/awayMatches)*100;
            $scope.teamBWinPrecentage = (wonMatches/totalMatches)*100;

            var teamBWinData = {
                labels: [
                    "Wins: " + wonMatches,
                    "Losses: " + lostMatches,
                    "Draws: " + drewMatches
                ],
                datasets: [
                    {
                        data: [wonMatches, lostMatches, drewMatches],
                        backgroundColor: [
                            "rgba(2, 22, 40, 1)",
                            "#A5B7CA",
                            "#FFCE56"
                        ],
                        hoverBackgroundColor: [
                            "rgba(2, 22, 40, 1)",
                            "#A5B7CA",
                            "#FFCE56"
                        ]
                    }]
            };
            var options = { tooltips: {enabled: false }};
            var teamBWinsCtx = document.getElementById("teamBWinsTable");
            var teamBWinsTable = new Chart(teamBWinsCtx, {
                type: 'pie',
                data: teamBWinData,
                options: options
            });
        });

});


