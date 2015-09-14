define(
[
    'app',

    // lib
    'backbone',

    // views
    'PrettifyView',
],

function (app, Backbone, PrettifyView) {

    'use strict';

    var GlobalRouter = Backbone.Router.extend({
        routes: {
            'words/:post/': 'blogPost',

            '*default': 'default',
        },
        blogPost: function () {
            this.announce({
                subviews: [PrettifyView]
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