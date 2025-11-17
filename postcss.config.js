// Use CommonJS because CRA's PostCSS loader expects a CJS config file.
// Use the separate `@tailwindcss/postcss` plugin as required by Tailwind.
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
