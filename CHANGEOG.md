# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/LandRegistry/govuk-frontend-wtf-demo/compare/1.4.0...main)

## [1.4.0](https://github.com/LandRegistry/govuk-frontend-wtf-demo/releases/tag/1.4.0) - 11/11/2021

### Changed

- Updated `govuk-frontend-wtf` to [release 1.1.0](https://github.com/LandRegistry/govuk-frontend-wtf/releases/tag/1.1.0)
- Updated `flask-wtf` to [release 1.0.0](https://github.com/wtforms/flask-wtf/releases/tag/v1.0.0)
- Updated `wtforms` to [release 3.0.0](https://github.com/wtforms/wtforms/releases/tag/3.0.0)


## [1.3.0](https://github.com/LandRegistry/govuk-frontend-wtf-demo/releases/tag/1.3.0) - 22/10/2021

### Added

- Support for [Python v3.10](https://www.python.org/downloads/release/python-3100/)

### Changed

- Updated `govuk-frontend-wtf` to [release 1.0.0](https://github.com/LandRegistry/govuk-frontend-wtf/releases/tag/1.0.0)
- Updated `govuk-frontend-jinja` to [release 1.5.1](https://github.com/LandRegistry/govuk-frontend-jinja/releases/tag/1.5.1)
- Updated `govuk-frontend` to [release 3.14.0](https://github.com/alphagov/govuk-frontend/releases/tag/v3.14.0)
- Updated `flask` to [release v2.0.2](https://flask.palletsprojects.com/en/2.0.x/changes/)
- Updated `jinja2` to [release v3.0.2](https://jinja.palletsprojects.com/en/3.0.x/changes/)
- Updated Python runtime to 3.9.7

### Removed

- Manual fieldsets and hints from template examples

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
