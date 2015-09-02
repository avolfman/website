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
        initialize: function (options) {
            this.$switches = this.$('.js-switch');
            this.$panels = this.$('.js-panel');
            this.title = options.title;

            if (!$.contains(document.documentElement, this.$el[0])) this.render();
            else this.transitionIn();

            this.listenTo(app.vent, 'page:requested', this.transitionOut);
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
            $('body').prepend(this.$el);
            document.title = this.title;

            app.reflow(this.$el);
            this.transitionIn();
        },
    });

    return PageView;

});