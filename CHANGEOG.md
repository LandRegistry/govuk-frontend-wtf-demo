# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/LandRegistry/govuk-frontend-wtf-demo/compare/1.2.0...main)

## [1.2.0](https://github.com/LandRegistry/govuk-frontend-wtf-demo/releases/tag/1.2.0) - 13/05/2021

### Changed

- Updated to use `govuk-frontend-wtf` [version 0.3.0](https://github.com/LandRegistry/govuk-frontend-wtf/releases/tag/0.3.0).

## [1.1.0](https://github.com/LandRegistry/govuk-frontend-wtf-demo/releases/tag/1.1.0) - 06/05/2021

### Added

- [Date input component](https://design-system.service.gov.uk/components/date-input/) added to "Create an account" and "Kitchen sink" example forms.
- Cookies page example form as per [GOV.UK Design System pattern](https://design-system.service.gov.uk/patterns/cookies-page/).

### Changed

- Updated to use `govuk-frontend-wtf` [version 0.2.0](https://github.com/LandRegistry/govuk-frontend-wtf/releases/tag/0.2.0), which adds support for the date input component.
- Over-ridden default CSRF error to return a notification banner rather than part of the form validation error summary.
- Put notification banner and error summary macros into the base template, which inherited templates can call with `{{ super() }}` inside the grid column width for their content.
- Formatting tweaks for improved readability.

## [1.0.0](https://github.com/LandRegistry/govuk-frontend-wtf-demo/releases/tag/1.0.0) - 25/02/2021

### Added

- First release of demo app showcasing how to use the GOV.UK Frontend WTForms package.
