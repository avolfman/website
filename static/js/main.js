// Copyright 2015 Matt Taube
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

require.config({
    paths: {
        // lib
        'almond': 'lib/almond',
        'backbone': 'lib/backbone',
        'jquery': 'lib/jquery',
        'underscore': 'lib/underscore',

        // routers
        // 'GlobalRouter': 'routers/GlobalRouter',
    },
    shim: {
        'underscore': { exports: '_' },
        'backbone': {
            deps: ['jquery', 'underscore'],
            exports: 'Backbone'
        },
    },
});

define(
[
    // lib
    'jquery',
    'backbone',

    // routers
    // 'GlobalRouter',
],

function($, Backbone) {

    var app = {
        // Global event aggregator
        vent: _.extend(Backbone.Events),
    }

    var GlobalRouter = Backbone.Router.extend({
        routes: {
            // 'contact/': 'contact',

            '*default': 'default',
        },
        initialize: function () {
            // console.log('GlobalRouter.initialize()');
            this.isFirstRoute = true;

            this.once('route', this.all);
        },

        default: function (event) {
            console.log('GlobalRouter.default()');

            if (!this.isFirstRoute) {
                app.vent.trigger('route:changed', window.location.href);
            }
        },

        all: function (event) {
            console.log('GlobalRouter.all()');
            this.isFirstRoute = false;
        }
    });

    var PageView = Backbone.View.extend({
        initialize: function () {
            console.log('PageView.initialize()');
        },
    });

    var contentMediator = {
        getContent: function (url) {
            console.log('contentMediator.getContent()');
            
            $.ajax({
                url: url,
                error: function (jqXHR, textStatus, errorThrown) {
                    debugger;
                },
                success: function (data, textStatus, jqXHR) {
                    $('.js-panelLeft').html(data.panelLeft)
                    $('.js-panelRight').html(data.panelRight)
                    document.title = data.pageTitle
                }
            })
        },
        createView: function () {

        }
    };

    app.vent.on('route:changed', contentMediator.getContent);




    new GlobalRouter();

    // Do not start Backbone.history until all routers have been initialized.
    if (Modernizr.history) {
        Backbone.history.start({
            hashChange: false,
            pushState: true,
            // root: glco.root,
            // trigger: true,
        });


        // Credit: https://gist.github.com/tbranyen/1142129
        // All navigation that is relative should be passed through the navigate
        // method, to be processed by the router. If the link has a `data-bypass`
        // attribute, bypass the delegation completely.
        $(document).on('click', 'a[href]:not([data-bypass])', function(event) {
            // Get the absolute anchor href.
            var href = {
                attr: $(this).attr('href'),
                prop: $(this).prop('href')
            };
            // Get the absolute root.
            var root = location.protocol + "//" + location.host;

            // Ensure the root is part of the anchor href, meaning it's relative.
            if (href.prop.slice(0, root.length) === root) {
                // Stop the default event to ensure the link will not cause a page
                // refresh.
                event.preventDefault();

                // Note by using Backbone.history.navigate, router events will not be
                // triggered.  If this is a problem, change this to navigate on your
                // router.
                Backbone.history.navigate(href.attr, true);
            }
        });
    }

});
