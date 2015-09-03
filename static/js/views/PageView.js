define(
[
    'app',

    // lib
    'jquery',
    'backbone',

    // plugins
    'jquery.transition'
],

function (app, $, Backbone) {

    'use strict';

    var PageView = Backbone.View.extend({
        el: '.js-page',
        initialize: function (options) {
            this.$switches = this.$('.js-switch');
            this.$panels = this.$('.js-panel');
            this.subviews = options.subviews;
            this.title = options.title;

            this.listenTo(app.vent, 'page:teardown', this.transitionOut);

            this.render();
        },
        transitionIn: function () {
            var i = 0;

            this.$panels.one(app.TRANSITION_END_EVENT, $.proxy(function () {
                i++;

                if (i == this.$panels.length) {
                    this.$el.removeClass('is-entering');

                    this.activateSwitches();
                }
            }, this)).emulateTransitionEnd(app.TRANSITION_SPEED);

            this.$el.addClass('is-active is-entering');
        },
        transitionOut: function () {
            var i = 0;

            this.$panels.one(app.TRANSITION_END_EVENT, $.proxy(function () {
                i++;

                if (i == this.$panels.length) this.remove();
            }, this)).emulateTransitionEnd(app.TRANSITION_SPEED);

            this.$el.addClass('is-exiting');
        },
        activateSwitches: function () {
            this.$switches.each(function (i, el) {
                setTimeout(function () { $(el).addClass('is-active'); }, 100 * i);
            });
        },

        render: function () {
            if (!$.contains(document.documentElement, this.$el[0])) {
                $('body').prepend(this.$el);
                document.title = this.title;

                app.reflow(this.$el);
            }

            if (this.subviews) {
                _.each(this.subviews, function (View, i, subviews) {
                    subviews[i] = new View();
                }, this);
            }

            this.transitionIn();

            return this;
        },
        remove: function () {
            _.each(this.subviews, function (view) {
                view.remove();
            });

            Backbone.View.prototype.remove.call(this);
        },
    });

    return PageView;

});