sportModule.service('teamSearchService', ['$http', function($http){
    return {
        search: function(keywords){
            console.log('/api/teams/search?team=' + keywords);
            return $http.get('/api/teams/search?team=' + keywords );
        }
    }
}]);