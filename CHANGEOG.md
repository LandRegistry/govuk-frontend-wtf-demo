# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/LandRegistry/govuk-frontend-wtf-demo/compare/1.0.0...main)

### Added

- Cookies page example form as per [GOV.UK Design System pattern](https://design-system.service.gov.uk/patterns/cookies-page/).

### Changed

- Over-ridden default CSRF error to return a notification banner rather than part of the form validation error summary.
- Put notification banner and error summary macros into the base template, which inherited templates can call with `{{ super() }}` inside the grid column width for their content.
- Formatting tweaks for improved readability.

## [1.0.0](https://github.com/LandRegistry/govuk-frontend-wtf-demo/releases/tag/1.0.0) - 25/02/2021

### Added

- First release of demo app showcasing how to use the GOV.UK Frontend WTForms package.
