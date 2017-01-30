# PISADataVisualization

## Summary

The PISA is an international study conducted to assess 15-year-olds' performances on math, reading, and science. Here, I created a visualization comparing the average scores within a country based on two home factors: the student having his/her own room; and the student having a computer. Each category is represented by an overlapping bar chart, allowing a simple visual comparison of scores. Almost across the board, having either of these correlated with an increased math score.

## Design

I chose to represent the data as bubble charts with the exception of the "no room, no computer" category in order to easily visualize the difference between having a room/computer and having neither. I tried using line charts, but the empty area below the lines seemed more confusing than clear. I also tried using area charts but reviewers commented that the overlapping areas muddled the data and the message. By implementing toggling of the scenarios, viewers can compare scenarios or inspect individual scenarios for further investigation of the data.

Originally, my bar chart had four scenarios: having a room, having a computer, having access to the internet, and none of the three. Due to feedback, I removed the internet chart as it almost 100% overlapped with the computer chart, and I also added a scenario for having both a room and a computer. I also tried adding a chart of the overall country averages (regardless of scenario) as a scatterplot as a point of contrast, but ended up removing it as it detracted from the overall explanatory message.

I intentionally omitted the x-axis title as the title makes it clear that the x-axis is individual countries. Various amounts of feedback caused me to try changing the opacity, but in the end, I found the default 0.8 value to be the best. I tried different ways of sorting the countries, including alphabetically and by internet-scores. In the end, sorting by the overall averages scatterplot had the most visual appeal, as you can immediately see how countries compare to one another before considering different home factors.

I started the y-axis from 0 because I didn't want to falsely convey that having access to a computer doubled scores in some cases. (The PISA scores are scaled such that the average is 500 and the standard deviation is 100.)

## Feedback

Feedback was obtained by uploading my visualization to gist. Four transcripts are as follows:

Tyler:
when you re click the latest legend block it brings it in the front
which usually covers up all the others
like if you reclick own room or internet it pops up and you cant see shit for the others
also left title should be bigger and bottom should have title
i mean i guess it works dpeending on what youre doing
the best thing to do is probably add a reset feature
which puts the original graph back
you cant see internet from original graph so you probably wouldnt send that message if someone looked at it
can you increase transparency or something
i mean thats fine but if you keep the other option i would probably increase transperancy
you could also change the y axis values to like 30 or 40 if it fits so the difference looks bigger

jeff:
on my browser when i click on a box i see a plot come up but it looks very faint
i think that's just a problem with my browser tho
otherwise i think it's pretty clear what you're plotting
looks like the default sorting is by internet highest to lowest average
is there

jacob:
it doesn't look like contiguous data
also lul what does none even mean
should you have a seperate category for yes-to-both


Udacity review:

Your current title: "PISA Math Averages Based on Home Environment by Country" s exploratory. It's telling the reader what the data is and leaving them free to explore it further.

As noted in one of your feedback comments, the areas currently overlap so it is very difficult to see whats going on. You need to have a rethink on how to present your key findings in a clearer way.

I've outlined some ideas below. I would suggest considering them, implementing those you think will work and then asking for further feedback to see the difference the changes have made.

You may need to repeat the change-feedback loop a couple of times before you get it right. Remember if you get stuck on any technical issues you can reach out to the Udacity Forum for assistance.

Below ideas to foster better communication between the reader and the visualisation:

-have the average as area (greyscale is a great idea for colour coding average but if area you could go a bit lighter) and the other variables as dots? You will hopefully be able to see which scores are above and below average more easily.

-group the countries into continents to get a wider overall picture - there are a lot of them and it's quite difficult to read. There could be the option to show both - by country or by continent.

-switch the x and the y axis.

One or a combination of the above should solve the problem.

## Resources

Background resources:
https://en.wikipedia.org/wiki/Programme_for_International_Student_Assessment

Programming resources:
http://dimplejs.org/advanced_examples_viewer.html?id=advanced_interactive_legends
http://stackoverflow.com/questions/25698268/dimple-js-d3-js-how-to-toggle-series

Link to visualization in gist:
https://gist.github.com/tigreryder/70c8f2fcfc1e653c6cd4351f35b21641
http://bl.ocks.org/tigreryder/70c8f2fcfc1e653c6cd4351f35b21641
