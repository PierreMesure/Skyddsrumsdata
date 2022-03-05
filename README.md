# Skyddsrumsdata

With the invasion of Ukraine and the resulting increase in tension with Russia, there has been a renewed interest in Sweden's total defence strategy (*totalförsvar*) and its degree of preparation (*beredskapen*). One of these aspects is the impressive number of shelters (*skyddsrum*) that have been built since the Second World War.

MSB is in charge of keeping track of them and has a cool online map called [Skyddsrumskarta](https://www.msb.se/sv/verktyg--tjanster/skyddsrumskarta/). It's probably the easiest tool you can find if you just want to find the shelters near you and some basic info such as their capacity.

They also claim to publish the data as open and it is possible to find it listed on [dataportal.se](https://www.dataportal.se/sv/datasets/778_21575) and [geodata.se](https://www.geodata.se/geodataportalen/srv/swe/catalog.search#/search?or=8343e110-6ea8-44ed-995d-93d6d4f1d47b). But the format and the ways the data is available makes it quite hard to reuse, especially if you are not used to GIS tools and the associated formats.

So I reached out for help on the Nordic Datajournalistik Facebook page and got a lot of great help. And I thought I'd help the people who will try this after me and write this little script that fetches the data and converts it to easily reusable formats (CSV, JSON and GeoJSON). As a bonus, I also added a Github Action that should try and update the data every month.
