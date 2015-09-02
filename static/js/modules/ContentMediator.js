define(
[
    'app',

    // lib
    'backbone',
    'underscore',

    // views
    'PageView',

    // plugins
    'jquery.scrollTo',
],

function (app, Backbone, _, PageView) {

    'use strict';

    var ContentMediator = function () {
        this.initialize.apply(this);
    };

    _.extend(ContentMediator.prototype, Backbone.Events, {
        initialize: function () {
            this.listenTo(app.vent, 'route:changed', this.changeContent);

            new PageView({ el: '.js-page' });
        },
        changeContent: function () {
            app.scrollTo(0, {
                always: $.proxy(this.requestContent, this)
            });
        },
        requestContent: function () {
            $.ajax({
                url: window.location.href,
                beforeSend: function () { app.vent.trigger('page:requested'); },
                error: function (jqXHR, textStatus, errorThrown) {
                    debugger;
                },
                success: $.proxy(function (data, textStatus, jqXHR) {
                    this.loadContent(data);
                }, this)
            });
        },
        loadContent: function (data) {
            new PageView(_.extend(data, { el: data.content }));
        }
    });

    return ContentMediator;

});