define(
[
    'app',

    // lib
    'backbone',

    // views
    'GoogleMapsView',
    'PrettifyView',
],

function (app, Backbone, GoogleMapsView, PrettifyView) {

    'use strict';

    var GlobalRouter = Backbone.Router.extend({
        routes: {
            'contact/': 'contact',
            'words/:post/': 'blogPost',

            '*default': 'default',
        },
        blogPost: function () {
            this.announce({
                subviews: [PrettifyView]
            });
        },
        contact: function (event) {
            this.announce({
                // subviews: [GoogleMapsView]
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