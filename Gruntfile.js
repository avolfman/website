module.exports = function (grunt) {

    var BASE_URL_CSS = 'static/built/css/';
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
        watch: {
            less: {
                files: [BASE_URL_LESS + '**/*.less'],
                tasks: ['less'],
            },
        },
    });

    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('build', [
        'less',
    ]);

};
