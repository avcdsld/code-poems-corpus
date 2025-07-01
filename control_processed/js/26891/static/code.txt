function pages() {
  return gulp.src(['src/pages/**/*.html', '!src/pages/archive/**/*.html'])
    .pipe(panini({
      root: 'src/pages',
      layouts: 'src/layouts',
      partials: 'src/partials',
      helpers: 'src/helpers'
    }))
    .pipe(inky())
    .pipe(gulp.dest('dist'));
}