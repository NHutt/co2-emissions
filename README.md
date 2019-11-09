# CO2 Emissions

Check the page out at https://nhutt-co2-emissions.herokuapp.com/co2-emissions

On the search page you can pick a country or region and see the relevant CO2 emission values from years 1960-2014.

On the browse page you can pick a year and view emissions per capita values for all available countries.

## Known issues:

When passing lists to Jinja templates, lists apparently turn into long strings, which is why I've utilized some hacky solutions which I know are pretty bad and which I by no means approve of in a professional context. If I was about to embark on a new similar project, I'd separate the backend and frontend properly.

For some reason even some country names in the .csv files contain ",", for example "Congo, Dem. Rep.". I assume that this is why the country labels in the browse page become progressively more and more skewed towards the bottom of the chart. It seems that there are more labels than there are actual data values but there may be other causes to this problem as well.

Also, given the nature of the data set, charts in the browse category are pretty horrible (you can't even see the bar for those countries that have comparatively very low emissions) but I didn't remove any countries for the sake of completeness, even though some kind of top 10 list would've made for better looking charts. Also the amount of decimals is all kinds of crazy which also causes the labels of the x-axis not to show anything else than "...".

On the search page i've made the decision of not displaying year labels on the x-axis of the charts since it looks very messy and to my knowledge Apexcharts doesn't support displaying only some of the labels. You can, however, still see the years both on the x-axis and in the popup box once you mouseover the chart.

I have no idea why the .csv files have no data at all after year 2014 but that appears to be the case even though the files have been downloaded in 2019.
