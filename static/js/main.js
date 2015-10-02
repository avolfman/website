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
        'jquery.easing': 'lib/jquery.easing',
        'jquery.scrollTo': 'lib/jquery.scrollTo',
        'jquery.transition': 'lib/jquery.transition',
        'prettify': 'lib/prettify',
        'underscore': 'lib/underscore',

        // modules
        'app': 'modules/app',
        'ContentMediator': 'modules/ContentMediator',

        // routers
        'GlobalRouter': 'routers/GlobalRouter',

        // views
        'GoogleMapsView': 'views/GoogleMapsView',
        'PageView': 'views/PageView',
        'PrettifyView': 'views/PrettifyView',
        'ScrollProgressView': 'views/ScrollProgressView',
    },
    shim: {
        'backbone': {
            deps: ['jquery', 'underscore'],
            exports: 'Backbone'
        },
        'jquery.easing': { deps: ['jquery'] },
        'jquery.scrollTo': { deps: ['jquery', 'jquery.easing'] },
        'jquery.transition': { deps: ['jquery'] },
        'prettify': { exports: 'prettyPrint' },
        'underscore': { exports: '_' },
    },
});

define(
[
    // lib
    'jquery',
    'backbone',
    'underscore',

    // modules
    'ContentMediator',

    // routers
    'GlobalRouter',
],

function($, Backbone, _, ContentMediator, GlobalRouter) {

    'use strict';

    new ContentMediator();
    new GlobalRouter();

    // Do not start Backbone.history until all routers have been initialized.
    if (Modernizr.history) {
        Backbone.history.start({
            hashChange: false,
            pushState: true,
            trigger: true,
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
                // triggered. If this is a problem, change this to navigate on your
                // router.
                Backbone.history.navigate(href.attr, true);

                if (_.isFunction(window.ga)) window.ga('send', 'pageview', href.attr);
            }
        });
    }

});
