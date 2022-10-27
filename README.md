## Overview

This repository contains Python notebooks that demonstrate how to interact with the Carbon public web service to generate cross-tabulation reports. The notebooks can be opened by Visual Studio Code, Jupyter and other Python notebook hosts where they provide a rich interactive experience using a mixture of code and formatted commentary text.

---

## Web Service

The Carbon cross-tabulation library is written using the Microsoft .NET software platform and therefore cannot be invoked directly from the Python runtime. A public web service has been created by [Red Centre Software][rcs] to act as a *bridge* between Python and Carbon. The web service follows standard REST style conventions and the API and Swagger documentation are available at this address:

<https://rcsapps.azurewebsites.net/plutonium/swagger/>

There is currently only one endpoint that has been customised for Python clients, but others many be published in the future to make more of the underlying API available to developers in a *Pythonic* manner.

> :star: Note &mdash; Initial research has proven that Python can make direct calls to the Carbon API via the [Python.NET][pynet] package, but this technique is not supported yet. Further research on this matter happen if there sufficient interest.

---

## Sample Notebooks

### :blue_book: 01 Simple Report

Converts two arrays of static data into a cross-tabulation dataframe through the service endpoint that has been customised for the simplest possible use by Python clients.

### :blue_book: 02 Cloud Job Report

Generates a dataframe report using data that is stored in a public cloud job.

### :blue_book: 03 SPSS to Heat Map Chart

A sophisticated example of how SPSS (.sav) file can be transformed into a cross-tabulation report and presented as an attractive colour-coded heat map chart.

[dotnet]: https://en.wikipedia.org/wiki/.NET
[rcs]: https://www.redcentresoftware.com/
[pynet]: http://pythonnet.github.io/