(function(){"use strict";angular.module("rcukApp",["ngCookies","ngResource","ngSanitize","ngRoute","ngAnimate"]).config(["$routeProvider","$locationProvider",function(a){return a.when("/",{templateUrl:"views/main.html",controller:"MainCtrl"}).when("/result/:searchTerm",{templateUrl:"views/result.html",controller:"ResultCtrl"}).when("/person/:id",{templateUrl:"views/person.html",controller:"PersonCtrl"}).otherwise({redirectTo:"/"})}])}).call(this),function(){"use strict";angular.module("rcukApp").controller("MainCtrl",["$scope","$location",function(a,b){return a.showResults=function(a){return console.log(a),b.path("/result/"+a)},a.popularSearches=["Cryopreservation","Nanoparticles","Graphene","Mechatronics","Superhydrophobic Surfaces","Statins","Gene therapy"]}])}.call(this),function(){"use strict";angular.module("rcukApp").factory("Search",["$http",function(a){return{query:function(b,c){return a.get("/search/"+b).success(function(a){return c.persons=a})}}}]).factory("Person",["$http","Project",function(a,b){return{get:function(c,d){return a.get("/api/persons/"+c).success(function(a){var e,f,g,h,i,j,k;if(null!=a.PI_PER)for(a.pi=[],j=a.PI_PER,f=0,h=j.length;h>f;f++)e=j[f],b.get(e,a.pi);if(null!=a.COI_PER)for(a.coi=[],k=a.COI_PER,g=0,i=k.length;i>g;g++)e=k[g],b.get(e,a.coi);return console.log("Person "+c,a),d.person=a})}}}]).factory("Project",["$http",function(a){return{get:function(b,c){return a.get("/api/projects/"+b).success(function(a){return console.log("Project "+b,a),c.push(a)})}}}])}.call(this),function(){"use strict";angular.module("rcukApp").controller("ResultCtrl",["$scope","Search","$routeParams","$location",function(a,b,c,d){return b.query(c.searchTerm,a),a.showPerson=function(a){return console.log(a._id.$oid),d.path("/person/"+a._id.$oid)}}])}.call(this),function(){"use strict";angular.module("rcukApp").directive("mynavbar",function(){return{restrict:"A",templateUrl:"views/myNavbar.html"}})}.call(this),function(){"use strict";angular.module("rcukApp").controller("PersonCtrl",["$scope","Person","$routeParams",function(a,b,c){return b.get(c.id,a)}])}.call(this);