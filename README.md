# xlr-reporting-plugin

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0b22c5f5e5b84e7d97ced3887f1d9c22)](https://www.codacy.com/app/istairbn/xlr-reporting-plugin?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=istairbn/xlr-reporting-plugin&amp;utm_campaign=Badge_Grade)

See the **[XL Release Documentation](https://docs.xebialabs.com/xl-release/index.html)** for background information on XL Release and release concepts.

# Overview# 
The xlr-reporting-plugin is a XL Release plugin that is intended to provide useful information that can be emailed to various stakeholders. Whist many users may wish to use the standard reporting tools, some users simply need a brief update on the status of the release.

## Installation #
Place the latest released version under the `plugins` dir. If needed append the following to the `script.policy` under `conf`:```permission java.io.FilePermission "plugins/*", "read";permission java.io.FilePermission "conf/logback.xml", "read";```This plugin requires XLR 5.5+

## Types ##
+ Timer
  * `Start Time`: Optional Input of a `Time Now` from another Timer Object  
  * `Time Now`: Outputs the current time in Python Time format
  * `Seconds Elapsed`: Optional Output. Provides the elapsed seconds between `Start Time` and `Time Now`
  * `Duration`: Optional Output. Provides the `Seconds Elapsed` in a human readable format, suitable for reporting purposes.

+ Status
  * `Status`: Output - provides a human readable output of current status, used for email dissemination.

+ Failures
  * `Total`: Output. Total count of Failures in the current release. 
  * `Current Phase`: Output. Count of failures in the current phase.
