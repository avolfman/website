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
        // Libraries
        'almond': 'lib/almond',
        'backbone': 'lib/backbone',
        'jquery': 'lib/jquery',
        'underscore': 'lib/underscore',

        // jQuery Plugins

        // Modules
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
    // Libraries
    'jquery',
    'backbone',
    'underscore',

    // Modules

    // jQuery Plugins
],

function($, Backbone, _) {

    var MediaPanelView = Backbone.View.extend({
        initialize: function (options) {
            this.listenTo(options.mediator, 'toggle:' + this.$el.attr('id'), this.toggle);
        },
        toggle: function () {
            this.$el.toggleClass('is-active');
        },
    });

    var MediaPanelMediator = Backbone.View.extend({
        initialize: function () {
            this.$triggers = $('.js-mediaPanelTrigger').on('mouseenter mouseleave', $.proxy(this.announceHover, this));

            $('.js-mediaPanel').each($.proxy(function (i, el) {
                new MediaPanelView({
                    el: el,
                    mediator: this
                });
            }, this));
        },
        announceHover: function (event) {
            var target = $(event.target).data('target');

            this.trigger('toggle:' + $(event.target).data('target'));
        },
    });

    if (!Modernizr.touch) new MediaPanelMediator();

});
