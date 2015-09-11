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
            this.$el.find('pre').addClass('prettyprint linenums');

            this.render();
        },
        render: function () {
            Prettify();
        },
    });

    return PrettifyView;

});