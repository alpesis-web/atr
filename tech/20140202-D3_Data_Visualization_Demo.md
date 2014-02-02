Feb 2 2014 | D3, Data_Visualization, js | Kelly Chan
# D3 Data Visualization Demo

### 1. Get Started

step1. \<header\> d3.js inclluded  
```
<script src="http://d3js.org/d3.v3.min.js" type="text/javascript" charset="utf-8"></script>
```
step2. \<body\> div included
```
    <div>1</div>
    <div>2</div>
    <div>3</div>
    <div>4</div>
    <div>5</div>
```
step3. \<body\> d3 script included
```
<script type="text/javascript">
    // select the divs and change the 'background-color' to 'steelblue';
    d3.selectAll("div").style("background-color","steelblue")
</script>
```
