/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./fines_heat_map/templates/**/*.html",
    "./fines_heat_map/**/templates/**/*.html",
    "./fines_heat_map/**/*.py",
  ],
  theme: {
    extend: {
      colors: {
        'fines-blue': '#0ea5e9',
        'fines-green': '#10b981',
        'fines-mint': '#6ee7b7',
        'fines-encabezado': '#3C5A80',
        'fines-encabezado-light': '#3C7780',
        'fines-encabezado-dark': '#2E4460',
      },
    },
  },
  plugins: [],
}

