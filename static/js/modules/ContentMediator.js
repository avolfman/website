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
            this.pageView = undefined;
            this.pageViewOptions = {}

            this.listenTo(app.vent, 'route', this.initializeContent);
        },
        initializeContent: function (options) {
            this.pageViewOptions = options;

            if (!this.pageView) this.initializePageView(options);
            else {
                app.scrollTo(0, {
                    always: $.proxy(this.requestContent, this, $.proxy(this.initializePageView, this))
                });
            }
        },
        initializePageView: function () {
            this.pageView = new PageView(this.pageViewOptions);
        },
        requestContent: function (callback) {
            $.ajax({
                dataType: 'json',
                beforeSend: function () { app.vent.trigger('page:teardown'); },
                error: function (jqXHR, textStatus, errorThrown) {
                    debugger;
                },
                success: $.proxy(function (data, textStatus, jqXHR) {
                    _.extend(this.pageViewOptions, data, { el: data.html })

                    callback();
                }, this),
                // Add fake URL parameter so that browser does not cache the AJAX / non-AJAX requests as the same.
                // Without it sometimes raw JSON is shown in the browser, i.e. when re-opening a closed tab.
                url: window.location.href + '?ajax=true',
            });
        },
    });

    return ContentMediator;

});