# Food for All - Public Transportation for Food Access
Analysis of public transportation to food sources from food deserts. 

Food for All website: https://fooddeserts01.herokuapp.com 

Languages, modules, packages, and tools used in this project:
geopy, 
FLASK,
Python,
Pandas,
Postgress, 
Logistic regression - MANOVA, ANOVA, Kmeans cluster,
Heroku,
Tableau,
scikitlearn,
HTML/CSS,
Javascript,

The purpose of this project is to both validate the concept of food desert status and to uncover the factors that determine whether a household belongs to a “food desert” designated census tract by initially looking at a particularly area of Maricopa county in Arizona. We seek to make an impact with this data by determining if the public transportation number, times and, locations of routes, and frequency of routes is sufficient to assist citizens living in the food deserts of Maricopa County to reach accessible, affordable food in an efficient manner. Depending on the outcome, this data may be helpful or and can be shared with government and non-profit organizations to act appropriately.

All sections of the project used data from the USDA Food Access Research Atlas, we considered several economic factors (i.e., poverty levels within the census tract), demographic factors (children, elders, or specific ethnicities in the population), and practical factors like number of grocery stores, percent of households with no vehicle, and number of bus stops within a tract. 

Python Pandas was used to read, clean, and organize data.

Bus Stop Data pulled by/from: 
  Using API for ARCOGIS for Valley Metro has a 50token a month limit. 
  Utilizing KML files. To read in KML files, ... utilizing direct geojson links (directly in file ..._create_artifact)
  ```
  $ pip install geopandas and fiona (if necessary)
  ```
  Using geopandas to read in your geojson file/url/api. 
  So as to not continue to make requests to host server (unless needing live data), utilize geopandas write function to write ```to_file("filename.geojson", Driver='geoJSON')     ```~after writing geopandas, environment stopped liking geopandas. Switching to read the geoJSON file back in with dependency geojson; index.html, container for JS script.        from index.html location, terminal code: `$ python -m http.server`

Food Desert Data pulled by/from: 
  Using Python Pandas to load data – 
  foodAccessData_csv = os.path.join('Resources', 'AZ Food Access Research Atlas.csv')

  Using Python SQL toolkit and Object Relational Mapper – creating postgress database.

Served up project on Heroku
 

An example of why this is important:

"New York (CNN Business)The coronavirus has made it harder for everyone to buy food
and other essential items under stay-at-home orders, social distancing guidelines and
limited delivery slots for online groceries.
But even before the pandemic, millions of people in the United States were struggling with
access to groceries — and the problem has gotten even worse for them."

"Beyond job loss or a drop in income, other factors during the pandemic have made it
harder for residents already struggling with access to low-priced meats and produce,
public health experts say.
Food prices have increased, stretching low-income residents' budgets. Overall, the price of
groceries grew 2.6% in April, the biggest month-to-month increase since 1974, according
to the Bureau of Labor Statistics. Egg prices shot up 16.1%, meat prices spiked 3.3% and
fruit and vegetables prices ticked up 1.5%.
"With the economic hit many people have taken over the last few months, it's tougher to
afford fresh, healthy food like fruits and veggies, which are more expensive than
processed items," said Michael Widener, geographer at the University of Toronto.
Additionally, online grocery delivery is out of reach for some customers who use food
stamps. Around 38 million Americans relied on food stamps last year, according to the
non-partisan Center on Budget and Policy Priorities." 

"In 2019, for the first time, the USDA gave the green light for food stamp recipients in New York
to use their benefits to buy groceries online and get them delivered to their homes. During the pandemic, the Agriculture Department has raced to allow more states to sign on to the online expansion of food stamps. But 15 states still do not allow customers to redeem benefits online." 

Retrieved from: 11/12/2020 Food deserts were a problem. The coronavirus has made them worse - CNN on 11/10/2020



