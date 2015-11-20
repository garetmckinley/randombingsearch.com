var gulp = require('gulp'),
    sass = require('gulp-sass'),
    minifyCSS = require('gulp-minify-css'),
    coffee = require('gulp-coffee'),
    minifyJS = require('gulp-uglify');

gulp.task('default', function() {
    gulp.src('src/sass/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('static/css'));

    gulp.src('src/coffee/*.coffee')
    .pipe(coffee())
    .pipe(minifyJS())
    .pipe(gulp.dest('static/js'));
});

gulp.task('heroku:prod', ['default']);
