define(
[
    // lib
    'jquery',
    'backbone',
    'prettify',
],

function ($, Backbone, Prettify) {

    'use strict';

    var PrettifyView = Backbone.View.extend({
        el: '.js-prettify',
        initialize: function () {
            Prettify();
        },
    });

    return PrettifyView;

});