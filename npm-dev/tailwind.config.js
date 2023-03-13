/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.html", "../**/templates/**/*.html"],
  theme: {
    extend: {},
    colors: {
      primary: {
        bg: "#0c4b33",
        fg: "#f1fff7",
        hover: "#3db78b",
      },
      light: {
        bg1: "#f8f8f8",
        bg2: "#eaeaea",
        bg3: "#bababa",
        fg: "#0c4b33",
      },
    },
  },
  plugins: [require("@tailwindcss/forms")],
};
