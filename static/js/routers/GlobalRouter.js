define(
[
    'app',

    // lib
    'backbone',

    // views
    'GoogleMapsView',
],

function (app, Backbone, GoogleMapsView) {

    'use strict';

    var GlobalRouter = Backbone.Router.extend({
        routes: {
            'contact/': 'contact',
            '*default': 'default',
        },
        contact: function (event) {
            this.announce({
                subviews: [GoogleMapsView],
            });
        },
        default: function (event) {
            this.announce();
        },

        announce: function (options) {
            app.vent.trigger('route', _.extend({}, options));
        },
    });

    return GlobalRouter;

});