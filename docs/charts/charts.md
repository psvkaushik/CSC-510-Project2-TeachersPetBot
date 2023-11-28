# About !chart

This command lets admins make a custom chart of any type with any size of dataset

# Location of Code

The code that implements the above mentioned gits functionality is located [here](https://github.com/chandur626/TeachersPetBot/blob/update-readme/src/bot.py).

# Code Description

## Functions

- def chart(ctx, title: str, chart: str, \*args): <br>
  This function creates a graph by getting the name of the chart, the type of chart the admin wants, data point count, data labels, and the data points for each data label.

# How to run it? (Small Example)

Enter space-separated: "!chart (name of the chart in 1 word) (type of chart {bar, line, doughnut, pie}) (Data labels {As Bs Cs Ds etc}) (Data points cooresponding to data labels)

FORMAT: !chart title (1 word), chart_type (pie, bar, line), name for Category 1, name for Category 2, name for Category N...(continue for however many categories there are), number for Category 1, number for Category 2, number for Category N..."
(continue for however many categories there are) EX. If # of categories is 5, there should be 5 category names and 5 category numbers"

```
!chart class_average_between_6_semesters bar S18 F18 S19 F19 S20 F20 90 91 92 93 94 95
```

Successful execution will show the custom chart

![customchart](https://github.com/chandur626/TeachersPetBot/blob/update-readme/docs/media/charts.gif)
