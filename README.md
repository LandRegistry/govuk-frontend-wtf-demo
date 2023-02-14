# GOV.UK Frontend WTForms Demo

Demo Flask app using [GOV.UK Frontend WTForms Widgets](https://github.com/LandRegistry/govuk-frontend-wtf).

> **IMPORTANT**: This app is deprecated. It is only meant to demonstate `govuk-frontend-wtf` based forms. It is not meant to be used as the basis for a full Flask app. If you are looking to build a fully featured Flask app that integrates with [GOV.UK Frontend WTForms](https://github.com/LandRegistry/govuk-frontend-wtf) and [GOV.UK Frontend Jinja](https://github.com/LandRegistry/govuk-frontend-jinja) please use the [GOV.UK Frontend Flask](https://github.com/LandRegistry/govuk-frontend-flask) template to [generate your app](https://github.com/LandRegistry/govuk-frontend-flask/generate) instead.

## Getting started

```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt ; pip3 install -r requirements_dev.txt
./build.sh
flask run
```
