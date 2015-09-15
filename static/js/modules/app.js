define(
[
    // lib
    'jquery',
    'backbone',
    'underscore',
],

function ($, Backbone, _) {

    'use strict';

    var app = {
        SCROLL_DURATION_MAX: 500,
        SCROLL_DURATION_MIN: 100,
        TRANSITION_END_EVENT: 'bsTransitionEnd',
        // Safety net in case transitionEnd event does not fire.
        TRANSITION_SPEED: 500,

        // Global event aggregator.
        vent: _.extend(Backbone.Events),

        // Triggers a reflow to force layout update.
        reflow: function ($el) {
            $el[0].offsetHeight;
        },
        // Smoothes the duration of scroll according to distance.
        scrollTo: function (target, options) {
            var $window = $(window);
            var defaultOptions = {
                easing: 'easeInOutCubic',
                interrupt: true,
            }
            var distance;
            var slope;

            if (_.isNumber(target)) {
                distance = Math.abs($window.scrollTop() - target);
                slope = (this.SCROLL_DURATION_MAX - this.SCROLL_DURATION_MIN) / 1000;

                _.extend(options, {
                    duration: Math.min(distance * slope + this.SCROLL_DURATION_MIN, this.SCROLL_DURATION_MAX)
                });
            }

            $window.scrollTo(target, _.extend(defaultOptions, options));
        },
    }

    return app;

});