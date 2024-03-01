# TSA-Software-Development-2024

## Inspiration
With so many crazy events in the world—from the pandemic, to inflation, to wars—it's easy to forget what we take for granted: Earth. Over the past few years, there have been increasingly more devastating and fluctuating weather events, whether it be fierce storms or scorching drought. Just last week, we saw record high-temperature heatwaves hit regions all across the globe, including Europe, Asia, and North America. In fact, according to the UN, we must reduce our carbon emissions by over 7% each year by 2030 to stop global temperature from rising 1.5 degrees Celsius over pre-industrial temperatures. Therefore, we were inspired to create WikiEnv to educate people on how climate change affects places worldwide and empower them to stop it.

## What it does
Our all-in-one website enables the user to search for any city, region, or country and returns a combination of formatted and embedded information. This information includes:
- Realtime weather data
- Suggestions on staying safe if current weather (especially air quality) is poor
- Embedded Wikipedia page displaying climate information on a given city
- Relief organizations around or relevant to the city
- Learn more section with charities relevant to the region that you can donate to

## How we built it
We used the Django framework with python, javascript, html, and css. The website backend is built with Django. It makes an API call to gather weather data and scrapes the web for relief organizations near the chosen city. Given this information, the backend code dynamically generates tips in inclement weather and loads embedded websites. The front end displays the information utilizing Django templating. The spinning globe in the background was modeled and rendered in Blender, a 3D modeling software.

## Challenges we ran into
Over the course of the hackathon, we had a plethora of challenges, some which made us even rethink our website design. The biggest issue we had was that initially we wanted to create a globe so that the user could click anywhere on it and get the information on a city. We tried to create this in Three js with webpackets to link to our backend. Unfortunately, we ran out of time and were unable to do this. However, we still managed to include a globe onto our website and set it to the website background by making a globe animation in Blender. Furthermore, as many of us never used Django before, the file structure was confusing and at times it made it extremely difficult to link files from on program to the next. Furthermore, since many of us did not know a lot of html or css, it was hard to get the embedded resources from formatting nicely, but we eventually got it done.

## Accomplishments that we're proud of
We are proud of creating an aesthetically pleasing, dynamically generated searchable website. We are especially proud of being able to scrape for relief organization websites relevant to any city in the world. We utilized our widespread knowledge of various resources and combined them into a single project.

## What we learned
We learned how to use Django, how to make API calls, and how to use javascript, html, css, and how to model and render in Blender. 

## What's next for WikiEnv
We hope that we can eventually get the Three js globe to work. We would like to also improve our webscraping to return more relevant results. 
