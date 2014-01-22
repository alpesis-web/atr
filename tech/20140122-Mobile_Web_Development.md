Jan 22 2014 | Mobile_Web_Development, HTML, CSS, API | Kelly Chan
# Mobile Web Development

### 1. Moible Web

Mobile Web = HTML/CSS/JS + APIs

### 2. Mobile Developer Tools

Chrome Dev Tool

### 3. Mobile UX and Viewport

```
<meta name="viewport" content="width=device-width, initial-scale=1">
```

CSS
```
|------------------------------------
| margin
|   |--------------------------------
|   | border                         
|   |   |----------------------------
|   |   | padding                    
|   |   |                            
|   |   |                             
|   |   |                            
```

### 4. Fluid Design

CSS: make reflow easy
```
{display: flex;}
```

### 5. Media Queries

CSS
```
.menu-items-grid{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    
    a {
        flex: 0 46%;
        position: relative;
    }
    
    @media (min-width: 500){
        a{
            flex: 0 24%;
        }
    }
}
```

column flex
```
.menu-items-grid{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: space-around;
    padding: 0 1%
}

@media (orientation:portrait){
    .menu-items-grid{
        flex-direction: column;
    }
}
```


### 6. Responsive Images

CSS3 image-set
```
background-image: image-set(url(low.png) 1x,
                            url(medium.png) 1.5x,
                            url(high.png) 2x);
```


### 7. Optimizing Performance

performance: network, compute, render

network
- # of bytes transferred
- how often we send requests
- power consumption
- max # of TCP connections

compute  
- memory constraint

render  
- framework

### 8. Touch

requestAnimationFrame

### 9. Input


### 10.
### 11.
### 12. 
