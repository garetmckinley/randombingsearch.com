var gulp = require('gulp'),
    sass = require('gulp-sass'),
    minifyCSS = require('gulp-minify-css'),
    coffee = require('gulp-coffee'),
    watch = require('gulp-watch'),
    minifyJS = require('gulp-uglify');

gulp.task('default', function() {
    gulp.src('src/sass/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(watch('src/sass/*.scss'))
    .pipe(gulp.dest('static/css'));

    gulp.src('src/coffee/*.coffee')
    .pipe(coffee())
    .pipe(minifyJS())
    .pipe(watch('src/coffee/*.coffee'))
    .pipe(gulp.dest('static/js'));
});

gulp.task('heroku:prod', ['default']);
