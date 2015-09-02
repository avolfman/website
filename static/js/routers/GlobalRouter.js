define(
[
    'app',

    // lib
    'backbone',
],

function (app, Backbone) {

    'use strict';

    var GlobalRouter = Backbone.Router.extend({
        routes: {
            '*default': 'default',
        },
        initialize: function () {
            this.isFirstRoute = true;

            this.once('route', this.all);
        },
        all: function (event) {
            this.isFirstRoute = false;
        },
        default: function (event) {
            if (!this.isFirstRoute) app.vent.trigger('route:changed');
        },
    });

    return GlobalRouter;

});