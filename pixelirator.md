# Introduction #

Pixelirator is a program for visualizing matrix data by using predefined the configuration and the color schema files. It generates PNG formatted images from text files of data.


# Details #

### Input and Output ###
  * Input data file
> Text format matrix data. For example, microarry data, clustering data, tklife data, and etc.
  * Configuration file -- [See detailed examples](http://pixelirator.googlecode.com/svn/wiki/SampleConfigure.wiki)
> Users can choose default configuration or specify a Configuration file to define the range and labels of the data, size and shape of a cell.
  * Color Map file -- [See detailed examples](http://pixelirator.googlecode.com/svn/wiki/sampleColorMap.wiki)
> Users can choose default a default color schema or specify a Color map file to define the flexible color schema.
  * Output image file
> PNG format.

### Example ###
  * Input data file
> This example uses the Effector in [Planta interaction data](http://pixelirator.googlecode.com/svn/wiki/data/EIP_4days_clustering.txt) from [the CHARGE Project](http://charge.ucdavis.edu/).

  * [Configuration file](http://pixelirator.googlecode.com/svn/wiki/data/config_charge.txt)

  * Color Map file
> [![](http://pixelirator.googlecode.com/svn/wiki/images/charge_colorbar_web.png)](http://pixelirator.googlecode.com/svn/wiki/data/colormap_charge.txt)

  * Output image file
> ![![](http://pixelirator.googlecode.com/svn/wiki/images/EIP_4days_sort_part_small.png)](http://pixelirator.googlecode.com/svn/wiki/images/EIP_4days_sort_part.png)

More samples can be found at [sample galley](http://pixelirator.googlecode.com/svn/wiki/sampleGalley.wiki)