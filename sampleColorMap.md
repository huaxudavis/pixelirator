## Color Map in Pixelirator ##

### What is in a Color Map ###

> A ''Color Map'' is a table that contains a list of input data and defines the color value corresponding to each data value.
The parameter of ''colormap'' in the configuration file has to be provided to specify the way that user defines the color map. There are three ways to define a color map.

1. Fixed:

> This is the most straightward way to define the color map. User specifies the color value for each distiguished data value. The data value can be numbers or other chararters.
> For example:

| data	| color value |
|:-----|:------------|
| 0    | FF0000      |
| 1    | 00FF00      |
| 2    | 00FFFF      |
| 3    | 0000FF      |

> As shown in the above table, the data value and the color value have one-to-one realtionship. The RANGE option is suitable for data that only have the fixed and limited values.

2. Range:

> The RANGE option can be used for more data points than the FIXED option. The data value has to be numbers. User set up colors for a set of ranges of data value.
> For example:
| data	| color value |
|:-----|:------------|
| min	 | FF0000      |
| 0	   | FFFF00      |
| 1	   | 00FF00      |
| 2	   | 00FFFF      |
| max	 | 0000FF      |

> As shown in the above table, data value less than 0 all has color value of FF0000, which is red; and data value between 0 and 1 has color value of FFFF00; and data value more than 2 has color value of 0000FF.

3. Rainbow:

> This option will assign the value semiatuomatically. User only needs to define the start, middle, and end point color, the program will calculate the color value for the rest of the data values based the function used choose to use.
> For example:
| data	| color value |
|:-----|:------------|
| -1	  | FF0000      |
| 0	   | 00FF00      |
| 1	   | 0000FF      |


> In the above table, user defines the color value for the start point: "-1", the middle point: "0", and the end point: "1". There could have more than one middle point. The color value for other data points will be calclulated by the following expression:

> `startpoint*(1-FUNC(currentpoint)) + endpoint*FUNC(currentpoint))`

> In this expression, the currentpoint is the data value of which color value need to be calcaluated. The startpoint is the color value of the largest data value in the color table that is smaller than the currentpoint. The endpoint is the color value of the smallest data value in the color tabble that is larger than the currentpoint. FUNC is the function that user choose to adjust the data.
There are 8 functions that are used to calculate the color value.
1 - linear;  2 - log<sub>2</sub>; 3 - ln; 4 - log<sub>10</sub>; 5 - sqrt; 6 - X<sup>2</sup>; 7 - X<sup>e</sup>; 8 - X<sup>3</sup>
See Example 4 about how to choose different functions to generate images.

### Color Type ###

**Color Type** specifies the way to express a color value.

> The parameter of **colortype** in the configuration file has to be provided to specify the way that user defines the color in the color map.
> There are two ways to define a color: **RGB** and **HEX**.

  * RGB:

> User define 3 values for R(Red), G(Green), B(Blue). Each value is from 0 to 255.
> For example:
| RED | R: 255; G: 0; B: 0 |
|:----|:-------------------|
| GREEN | R: 0; G: 255; B: 0 |
| BlUE | R: 0; G: 0; B: 255 |

  * HEX:

> User define Hexdecimal value for RGB. Color value consists 6 numbers, each number is from 0 to F.
> For example:
| RED | FF0000 |
|:----|:-------|
| GREEN | 00FF00 |
| BLUE | 0000FF |

### How to treat data out of range? ###

> In the FIXED option, user can specify a data value of default, any data value which can not be found in the color map will be assign to this value. In the RANGE option, user specify two values: MIN and MAX, which are defined for the data value too small or too large. In the RAINBOW option, the start and end point just like the MIN and MAX in the RANGE option.

## Examples of Color Map ##

### Example 1 ###

> The following examples demonstrate color maps by using the **Fixed** option.

#### Map1 ####

> This example used the color schema from [the CHARGE Project](http://charge.ucdavis.edu/) to illustrate the mapping from the interaction data to the color.

|![http://pixelirator.googlecode.com/svn/wiki/images/colorbar_charge.png](http://pixelirator.googlecode.com/svn/wiki/images/colorbar_charge.png)|![http://pixelirator.googlecode.com/svn/wiki/images/colormap_charge.png](http://pixelirator.googlecode.com/svn/wiki/images/colormap_charge.png) |
|:----------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|

#### Map2 ####

> This example illustrates the color schema of the **amino acids**.

|![http://pixelirator.googlecode.com/svn/wiki/images/colorbar_amino.png](http://pixelirator.googlecode.com/svn/wiki/images/colorbar_amino.png)|![http://pixelirator.googlecode.com/svn/wiki/images/colormap_amino.png](http://pixelirator.googlecode.com/svn/wiki/images/colormap_amino.png) |
|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|

### Example 2 ###

> The following examples demonstrate generate color maps by using the **Range** option.

#### Map3 ####

|![http://pixelirator.googlecode.com/svn/wiki/images/colorbar_Range.png](http://pixelirator.googlecode.com/svn/wiki/images/colorbar_Range.png)|![http://pixelirator.googlecode.com/svn/wiki/images/colormap_Range.png](http://pixelirator.googlecode.com/svn/wiki/images/colormap_Range.png) |
|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------|

### Example 3 ###

> The following 5 examples demonstrate color maps by using the **Rainbow** option. The color bar is calculated by using **linear** function.

#### Map1 ####
|![http://pixelirator.googlecode.com/svn/wiki/images/colorbar1.png](http://pixelirator.googlecode.com/svn/wiki/images/colorbar1.png)<br />  Color goes through 5 color points:<br />  Red - Yellow - Green - Cyan - Blue|![http://pixelirator.googlecode.com/svn/wiki/images/colormap1.png](http://pixelirator.googlecode.com/svn/wiki/images/colormap1.png) |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|

#### Map2 ####

|![http://pixelirator.googlecode.com/svn/wiki/images/colorbar2.png](http://pixelirator.googlecode.com/svn/wiki/images/colorbar2.png)<br />  Color goes through 4 color points:<br />  Yellow - Green - Cyan - Blue|![http://pixelirator.googlecode.com/svn/wiki/images/colormap2.png](http://pixelirator.googlecode.com/svn/wiki/images/colormap2.png) |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|

#### Map3 ####

|![http://pixelirator.googlecode.com/svn/wiki/images/colorbar3.png](http://pixelirator.googlecode.com/svn/wiki/images/colorbar3.png)<br />  Color goes through 3 color points:<br />  Green - Cyan - Blue|![http://pixelirator.googlecode.com/svn/wiki/images/colormap3.png](http://pixelirator.googlecode.com/svn/wiki/images/colormap3.png) |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|

#### Map4 ####

|![http://pixelirator.googlecode.com/svn/wiki/images/colorbar4.png](http://pixelirator.googlecode.com/svn/wiki/images/colorbar4.png)<br />  Color goes through 3 color points:<br />  Red - Yellow - Green|![http://pixelirator.googlecode.com/svn/wiki/images/colormap4.png](http://pixelirator.googlecode.com/svn/wiki/images/colormap4.png) |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|

#### Map5 ####

|![http://pixelirator.googlecode.com/svn/wiki/images/colorbar5.png](http://pixelirator.googlecode.com/svn/wiki/images/colorbar5.png)<br />  Color goes through 3 color points:<br />  Red - Green - Black - Red|![http://pixelirator.googlecode.com/svn/wiki/images/colormap5.png](http://pixelirator.googlecode.com/svn/wiki/images/colormap5.png) |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|

### Example 4 ###

> The following 3 examples demonstrate how to generate Rainbow color maps by using the different functions.
> These example use the [clustering data](http://www.atgc.org/XLinkage/MadMapper/arabidopsis/DL_RIL_LG4A.list.good.map.out.matrix2d.tab) from [the MapMapper](http://www.atgc.org/XLinkage/MadMapper/).
> There are 8 functions that are used to calculate the color value.
  1. - linear;  2 - log<sub>2</sub>; 3 - ln; 4 - log<sub>10</sub>; 5 - sqrt; 6 - X<sup>2</sup>; 7 - X<sup>e</sup>; 8 - X<sup>3</sup>
> In these example, the Color map defines 4 data points to demonstrate 3 of the functions.

#### Map1 ####

|![http://pixelirator.googlecode.com/svn/wiki/images/DL_colorbar1.png](http://pixelirator.googlecode.com/svn/wiki/images/DL_colorbar1.png)<br />  This color map was generated by using the **Linear** function |![![](http://pixelirator.googlecode.com/svn/wiki/images/DL_colormap1_thumb.png)](http://pixelirator.googlecode.com/svn/wiki/images/DL_colormap1.png) |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|

#### Map2 ####

|![http://pixelirator.googlecode.com/svn/wiki/images/DL_colorbar4.png](http://pixelirator.googlecode.com/svn/wiki/images/DL_colorbar4.png)<br />  This color map was generated by using the **Log<sub>10</sub>** function |![![](http://pixelirator.googlecode.com/svn/wiki/images/DL_colormap4_thumb.png)](http://pixelirator.googlecode.com/svn/wiki/images/DL_colormap4.png) |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|

#### Map3 ####

|![http://pixelirator.googlecode.com/svn/wiki/images/DL_colorbar5.png](http://pixelirator.googlecode.com/svn/wiki/images/DL_colorbar5.png)<br />  This color map was generated by using the **Sqrt** function |![![](http://pixelirator.googlecode.com/svn/wiki/images/DL_colormap5_thumb.png)](http://pixelirator.googlecode.com/svn/wiki/images/DL_colormap5.png) |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|