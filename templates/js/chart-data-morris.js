// First Chart Example - Area Line Chart

Morris.Area({
  // ID of the element in which to draw the chart.
  element: 'morris-chart-area',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
	{% for dataID in morris_chart_data.data %}
	{ key: '{{dataID.0}}', value: {{dataID.1}} },
    {% endfor %}
  ],
  // The name of the data record attribute that contains x-axis.
  xkey: 'key',
  // A list of names of data record attributes that contain y-axis.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['{{morris_chart_data.y_label}}'],
  // Disables line smoothing
  smooth: {{morris_chart_data.smooth}},
});

Morris.Donut({
  element: 'morris-chart-donut',
  data: [
    {label: "Referral", value: 42.7},
    {label: "Direct", value: 8.3},
    {label: "Social", value: 12.8},
    {label: "Organic", value: 36.2}
  ],
  formatter: function (y) { return y + "%" ;}
});

Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'morris-chart-line',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: [
    {% for dataID in morris_chart_data.data %}
    { key: '{{dataID.0}}', value: {{dataID.1}} },
    {% endfor %}
  ],
  // The name of the data record attribute that contains x-axis.
  xkey: 'key',
  // A list of names of data record attributes that contain y-axis.
  ykeys: ['value'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['{{morris_chart_data.y_label}}'],
  // Disables line smoothing
  smooth: {{morris_chart_data.smooth}},
});

Morris.Bar ({
  element: 'morris-chart-bar',
  data: [
	{device: 'iPhone', geekbench: 136},
	{device: 'iPhone 3G', geekbench: 137},
	{device: 'iPhone 3GS', geekbench: 275},
	{device: 'iPhone 4', geekbench: 380},
	{device: 'iPhone 4S', geekbench: 655},
	{device: 'iPhone 5', geekbench: 1571}
  ],
  xkey: 'device',
  ykeys: ['geekbench'],
  labels: ['Geekbench'],
  barRatio: 0.4,
  xLabelAngle: 35,
  hideHover: 'auto'
});
