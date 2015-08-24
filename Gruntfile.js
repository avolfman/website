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

module.exports = function (grunt) {

    var BASE_URL_CSS = 'static/built/css/';
    var BASE_URL_JS = 'static/js/';
    var BASE_URL_BUILT_JS = 'static/built/js/';
    var BASE_URL_LESS = 'static/less/';

    grunt.initConfig({
        less: {
            options: {
                compress: true,
            },
            default: {
                files: [
                    {
                        dest: BASE_URL_CSS + 'main.css',
                        src: BASE_URL_LESS + 'main.less',
                    },
                ]
            },
        },
        modernizr: {
            dist: {
                'devFile': 'remote',

                // Path to save out the built file.
                'outputFile': BASE_URL_BUILT_JS + 'lib/modernizr.js',
                'extra': {
                    'shiv': true,
                    'printshiv': false,
                    'load': false,
                    'mq': true,
                    'cssclasses': true,
                },
                'extensibility': {
                    'addtest': false,
                    'prefixed': false,
                    'teststyles': false,
                    'testprops': false,
                    'testallprops': false,
                    'hasevents': false,
                    'prefixes': false,
                    'domprefixes': false,
                    // 'cssclassprefix': ''
                },
                'uglify': true,
                'tests': [
                    'csstransforms',
                    'csstransforms3d',
                    'csstransitions',
                    'prefixed',
                    'opacity',
                    'touch'
                ],
                'parseFiles': false,
                'matchCommunityTests': false,
                'customTests': []
            }
        },
        requirejs: {
            options: {
                baseUrl: BASE_URL_JS,
                mainConfigFile: BASE_URL_JS + 'main.js',
            },
            default: {
                options: {
                    name: 'main',
                    out: BASE_URL_BUILT_JS + 'main.js',
                    exclude: [],
                    include: ['almond']
                }
            },
        },
        watch: {
            less: {
                files: [BASE_URL_LESS + '**/*.less'],
                tasks: ['less'],
            },
        },
    });

    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-modernizr');
    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('build', [
        'less',
        'modernizr',
        'requirejs',
    ]);

};
