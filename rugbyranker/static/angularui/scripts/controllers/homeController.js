sportModule.controller('homeController', function ($scope, $http, $location) {

    $http.get("api/home/articles/")
        .then(function (response) {
            $scope.articles = response.data;
        });
    $http.get("api/home/rankings/")
        .then(function (response) {
            $scope.rankings = response.data;
        });

    $http.get("/api/home/details/")
        .then(function (response) {
            $scope.details = response.data;
        });

    $http.get("/api/home/matches/")
        .then(function (response) {
            $scope.matches = response.data;
        });

    $http.get("/api/home/featured/")
        .then(function (response) {
            $scope.featured = response.data;
        });

    $scope.clickrank = function (id) {
        console.log($location.path("teams/" + id))
    };

    $scope.clickfeatured = function (id) {
        console.log($location.path("teams/" + id))
    };

});


sportModule.controller('navController', function ($scope, $http, $location) {

    $scope.menuItems = [
        {
            name: "Rankings",
            link: "/rankings",
            icon: "fa-list-ol"
        },

        //{
        //    name: "News",
        //    link: "/articles",
        //    icon: "fa-newspaper-o"
        //},
        {
            name: "Teams",
            link: "/teams",
            icon: "fa-users"
        },
        {
            name: "Comparison",
            link: "/comparison",
            icon: "fa-pie-chart"
        },
        {
            name: "Countries",
            link: "/countries",
            icon: "fa-flag"
        },
        {
            name: "Tournaments",
            link: "/tournaments",
            icon: "fa-trophy"
        }
    ];

    $scope.navshow = function () {
        $("#datadropdown").slideToggle();
    };

    $scope.navhide = function () {
        $("#datadropdown").hide();
    };

    $scope.setActive = function (menuItem) {
        $scope.activeMenu = menuItem;
    };
});