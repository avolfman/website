define(
[
    // lib
    'jquery',
    'backbone',
],

function ($, Backbone) {

    'use strict';

    var GoogleMapsView = Backbone.View.extend({
        el: '.js-googleMap',
        initialize: function (options) {
            window.renderGoogleMapsView = $.proxy(this.render, this);

            if (_.isUndefined(window.google)) require(['https://maps.googleapis.com/maps/api/js?key=AIzaSyC-rJppTvqtI7_YaRhPKC2e_-tWwGtEYU4&callback=renderGoogleMapsView']);
            else this.render();
        },
        render: function () {
            var venice = {
                lat: 33.990973,
                lng: -118.466945
            };
            var map = new google.maps.Map(this.$el[0], {
                center: venice,
                zoom: 12
            });

            new google.maps.Circle({
              strokeColor: '#f2f1f0',
              strokeOpacity: 0.8,
              strokeWeight: 2,
              fillColor: '#f2f1f0',
              fillOpacity: 0.35,
              map: map,
              center: venice,
              radius: 4000
            });
        },
    });

    return GoogleMapsView;

});