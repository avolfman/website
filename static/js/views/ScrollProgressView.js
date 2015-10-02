define(
[
    'app',

    // lib
    'jquery',
    'backbone',
],

function (app, $, Backbone) {

    'use strict';

    var ScrollProgressView = Backbone.View.extend({
        el: '.js-scrollProgressBar',
        initialize: function () {
            if (Modernizr.touch) return;
            this.$window = $(window);
            this.totalDistance = 9999;

            setTimeout($.proxy(function () {
                this.totalDistance = this.$el.closest('.js-page').height() - this.$window.height();

                this.$window.on('scroll', _.throttle($.proxy(this.handleScroll, this), 50));
            }, this), 250);
        },
        handleScroll: function (event) {
            var scrollTop = this.$window.scrollTop();
            var progress = scrollTop / this.totalDistance;

            this.$el.css('height', progress * 100 + '%');

            return this;
        },
        remove: function () {
            this.$window.off('scroll');

            Backbone.View.prototype.remove.call(this);
        },
    });

    return ScrollProgressView;

});