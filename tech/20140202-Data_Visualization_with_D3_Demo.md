Feb 2 2014 | D3, Data_Visualization, js | Kelly Chan
# Data Visualization with D3 (Demo)

### 1. Get Started

step1. \<header\> d3.js is added in the header
```
<script src="http://d3js.org/d3.v3.min.js" type="text/javascript" charset="utf-8"></script>
```
step2. \<body\> div is added in the body
```
    <div>1</div>
    <div>2</div>
    <div>3</div>
    <div>4</div>
    <div>5</div>
```
step3. \<body\> d3 script is written in the body
```
<script type="text/javascript">
    // select the divs and change the 'background-color' to 'steelblue';
    d3.selectAll("div").style("background-color","steelblue")
</script>
```

### 2. Binding Data

bind the `div`s with data [25,30,35,40,45], then set the `width` to be the coresponding data
```
d3.selectAll("div")  // select divs
  .data([25,30,35,40,45]) // binding data
  .style("width",function(d){return d + "px";}); // set width to be coresponding data
```

### 3. Add Some Animation
use `transition` to add animation. Use `duration` to set duration as 3000ms
```
d3.selectAll("div")
  .data([25,30,35,40,45])
  .transition() // animation
  .duration(3000) // set duration
  .style("width",function(d){return d + "px";});
  
```

FULL Script
```
<!DOCTYPE html>
<html>
<head>
<meta charset=utf-8 />
<title>d3 js beginning</title>
    <script src="http://d3js.org/d3.v3.min.js" type="text/javascript" charset="utf-8"></script>
    <style type="text/css">
        div{
            background-color: #dd9;
            margin: 5px;
            font-size: 25px;
            color: #007;
            padding: 10px;
           }
    </style>
</head>
<body>
    <div>D3 is cool!</div>
    <div>D3 is awesome!</div>
    <div>D3 is good!</div>
    <div>D3 is pretty!</div>
    <div>D3 is helpful!</div>

    <script type="text/javascript">
        d3.selectAll("div")
          .data([200,300,400,500,600])
          .transition()
          .duration(2000)
          .style("width", function(d) { return  d + "px"; });
    </script>
</body>
</html>
```


### 4. Enter and Exit

Use `d3.selectAll` to select all the circles and change their radius to 10 times of its index
```
d3.selectAll("circle")
    .attr("r",function(d,i){return (i+1)*10}); 
```
