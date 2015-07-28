## Configuration in Pixelirator ##

### List of Configuration Parameters ###

1. Parameters for Figures:
User defines the shape, size, color and borders of the cells, as well as the title, colorbar, and label of the figures

  * Define size, shape, and color.

| cell\_size | Pixel dimensions per cell as x, y (Default = 15, 15) |
|:-----------|:-----------------------------------------------------|
| cell\_space | Pixel gap between two cells (Default = 1)            |
| cell\_shape | Ellipse or rectangle (Default = rectangle)           |
| background\_color | Color for background (Default = 255, 255, 255)       |
| border\_exist | Draw border between cells: Y(Yes), N(No). (Default = Y) |
| border\_color | Color for border (Default = 0, 0, 0)                 |
| space\_size | Pixel space outside the image (Default = 20, 20)     |

  * Define the title, labels and color bar.

| title\_pos | Position of the title: U(Upper), D(Down), L(Left), R(Right) or N(No title). (Default = N) |
|:-----------|:------------------------------------------------------------------------------------------|
| title\_text | The content of the title. (Default = Test Image)                                          |
| bar\_pos   | Position of the colorbar: U(Upper)or N(No Color bar). (Default = N)                       |
| bar\_size  | Pixel dimensions per bar as x, y (Default = 5, 20)                                        |
| xlabel\_pos | Position of the Column label: U(Upper), D(Down) or N(No label for Columns). (Default = N) |
| ylabel\_pos | Position of the Row label: L(Left), R(Right) or N(No label for Rows). (Default = N)       |
| xlabel\_type | The content of the Column label: scale or header. (Default = header)                      |
| ylabel\_type | The content of the Row label: scale or header. (Default = header)                         |
| label\_color | Color for Label: (Default: 0, 0, 0)                                                       |
| print\_value | Print the data value in the cell: Y(Yes), N(No). (Default: N)                             |

See more examples of configurations below.

2. Parameters for Color map:
User specifies the type of a color map and the way to specify a color.

| colortype | Use Hexdecimal or RGB value to define a color. (Default = RGB) |
|:----------|:---------------------------------------------------------------|
| maptype   | Use one of three color map type: Rainbow, Range, and Fixed. (Default = Rainbow) |
| mapfunc   | Defines the function used to calculate color value when maptype is Rainbow. |

See [examples of color map](http://pixelirator.googlecode.com/svn/wiki/sampleColorMap.wiki) for details.

3. Parameters for Input Data file
User sets up the parameters to retrieve the labels and data.

| delimiter  | Delimiter to parse the data in a row(Default = TAB) |
|:-----------|:----------------------------------------------------|
| rowstart   | Index of the first row of the data(Default = 1)     |
| colstart   | Index of the first column of the data(Default = 1)  |
| xlabelat   | Index of the label of row(Default = 0)              |
| ylabelat   | Index of the label of column(Default = 0)           |

## Examples of Configuration ##

The following 4 examples demonstrate configurations by using the data from [the CHARGE project](http://charge.ucdavis.edu/).

### Example1 ###

![http://pixelirator.googlecode.com/svn/wiki/images/2days-6.png](http://pixelirator.googlecode.com/svn/wiki/images/2days-6.png)
  * cell\_shape = rectangle
  * cell\_size = 15, 15
  * cell\_space = 0
  * title\_pos = U
  * title\_text = Charge\_2\_days\_interaction Table
  * bar\_pos = Ubar\_size = 60, 9
  * xlabel\_type = scale
  * xlabel\_pos = D
  * ylabel\_type = header
  * ylabel\_pos = R
  * border\_exist = N
  * background\_color = 255, 255, 255
  * label\_color = 0, 0, 0
  * colortype = HEX
  * mapfunc = Fixed


### Example2 ###

![http://pixelirator.googlecode.com/svn/wiki/images/2days-2.png](http://pixelirator.googlecode.com/svn/wiki/images/2days-2.png)
  * cell\_shape = rectangle
  * cell\_size = 12, 12
  * cell\_space = 0
  * title\_pos = U
  * title\_text = Charge\_2\_days\_interaction Table
  * bar\_pos = N
  * xlabel\_type = header
  * xlabel\_pos = U
  * ylabel\_type = header
  * ylabel\_pos = L
  * border\_exist = Y
  * border\_color=196, 196, 196
  * background\_color = 255, 255, 255
  * label\_color = 0, 0, 0
  * colortype = HEX
  * mapfunc = Fixed



### Example3 ###

![http://pixelirator.googlecode.com/svn/wiki/images/2days-3.png](http://pixelirator.googlecode.com/svn/wiki/images/2days-3.png)
  * cell\_shape = ellipse
  * cell\_size = 12, 12
  * cell\_space = 0
  * title\_pos = U
  * title\_text = Charge\_2\_days\_interaction Table
  * bar\_pos = N
  * xlabel\_type = header
  * xlabel\_pos = U
  * ylabel\_type = header
  * ylabel\_pos = L
  * border\_exist = N
  * background\_color = 196, 196, 196
  * label\_color = 0, 0, 0
  * colortype = HEX
  * mapfunc = Fixed


### Example4 ###

![http://pixelirator.googlecode.com/svn/wiki/images/2days-5.png](http://pixelirator.googlecode.com/svn/wiki/images/2days-5.png)
  * cell\_shape = ellipse
  * cell\_size = 11, 11
  * cell\_space = 1
  * title\_pos = D
  * title\_text = Charge\_2\_days\_interaction Table
  * bar\_pos = N
  * xlabel\_type = header
  * xlabel\_pos = U
  * ylabel\_type = scale
  * ylabel\_pos = L
  * border\_exist = N
  * background\_color = 0, 0, 0
  * label\_color = 0, 150, 0
  * colortype = HEX
  * mapfunc = Fixed