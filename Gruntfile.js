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
    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('build', [
        'less',
        'requirejs',
    ]);

};
