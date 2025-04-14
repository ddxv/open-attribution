# Open Attribution

An open source Mobile Measurement Platform (MMP) for tracking your mobile advertising spend and ROI.

## ️️🏗️ Under Construction 🏗️

If you're interested in this project please reach out for collaboration or more info. [Chat on Discord](https://discord.gg/Z5ueYE3Ct3). OpenAttribution is aiming to have an alpha MVP but is not yet ready for production use. We would love if you can help with testing or development!

## Description

[OpenAttribution](https://openattribution.dev) is an open source mobile measurement platform (MMP) that tracks your mobile advertising spend from the ad impression or click and connects to later in-app events.

## Goal: True ownership of your mobile app's data

Developers should OWN their advertising data without needing to give it over to a 3rd party data collector just to buy mobile ads. Our goal is to give developers their own ad tracking software so that they don't need to rely on a 3rd party. When users click on an app ad it goes to your domain.

Paying someone else to hold and manage your app's data takes power away from app creators. Open Attribution is a suite of open source tools so that you can manage your advertising data ownership.

### This is done with several parts:

1. Impression, Click & Event Tracking on YOUR domain
   1. `apps/postback-api`
2. Attribution of Mobile users and events to the impressions or clicks
   1. `apps/analytics-db`
      1. SQL in Clickhouse
      2. Ability for clients to set their own SQL for custom attribution logic
3. In-App Event Tracking SDKs
   1. [OpenAttribution/oa-ios-sdk](https://github.com/OpenAttribution/oa-ios-sdk)
   2. [OpenAttribution/oa-android-sdk](https://github.com/OpenAttribution/oa-android-sdk)
4. Analytics Dashboard & Admin Panels
   1. `apps/dash-backend`
   2. `apps/dash-frontend`
   3. `apps/backend-db`

## Open Source Community

Why Open Source? Working in the open lets all parties see how attributing works and have input on it's logic.

## Interested in getting involved?

🏗️ We'd love help building and testing. You can reach out on [Discord](https://discord.gg/Z5ueYE3Ct3) or email [hello@openattribution.dev](mailto:hello@openattribution.dev)

To read the work in progress documentation head to [Open Attribution Docs](https://openattribution.dev/docs/) to learn more.

## Why do apps NEED attribution?

If you want to buy in-app advertisements attribution a technical requirement, not a business option. Apps cannot use regular HTTP Urls to connect users, deep links are too limited. Historically MMPs stepped in to help solve this complex problem but by doing so became the arbiters of large amounts of data that some apps may wish to maintain control over. Read more about the [historical background here](https://openattribution.github.io/open-attribution/about/history).
