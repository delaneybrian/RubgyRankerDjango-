sportModule.controller('homeController', function ($scope, $http, $location) {

    $http.get("api/home/articles/")
        .then(function (response) {
            $scope.articles = response.data;
            var articles = response.data;
            var i = 0;
            articles.forEach(function(element) {
                addSlide(i, element);
                i++;
            });
            console.log("Http Sucess");
            console.log(response.data);
        });

    $scope.myInterval = 5000;
    $scope.noWrapSlides = false;
    $scope.active = 0;
    var slides = $scope.slides = [];
    var currIndex = 0;

    addSlide = function (i, element) {
        console.log(element.mainheading);
        slides.push({
            image: element.mainimage,
            articleId: element.id,
            text: element.mainheading,
            date: element.date,
            id: i
        });
    };







    $http.get("api/home/rankings/")
        .then(function (response) {
            $scope.rankings = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/home/details/")
        .then(function (response) {
            $scope.details = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/home/matches/")
        .then(function (response) {
            $scope.matches = response.data;
            console.log("Http Sucess");
            console.log(response.data);
        });

    $http.get("/api/home/featured/")
        .then(function (response) {
            $scope.featured = response.data;
            console.log("Http Sucess");
            console.log(response.data);
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
        {
            name: "News",
            link: "/articles",
            icon: "fa-newspaper-o"
        },
        {
            name: "Teams",
            link: "/teams",
            icon: "fa-users"
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
        console.log($scope.activeMenu);
    };

});