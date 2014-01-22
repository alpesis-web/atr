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
