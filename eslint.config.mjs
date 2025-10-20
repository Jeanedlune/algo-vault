export default [
  {
    files: ["**/*.js"],
    ignores: [
      "**/*.ts",
      "**/*.go",
      "**/*.py",
      "**/*.cs",
      "**/*.cpp",
      "**/*.hpp",
      "**/*.cc",
      "node_modules/",
      "dist/",
      "build/",
      ".serena/",
    ],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
    },
    rules: {
      "no-unused-vars": "warn",
      "no-undef": "off",
      "no-console": "off",
    },
  },
];
