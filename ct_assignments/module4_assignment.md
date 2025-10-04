## Image filtering involves the application of window operations that perform useful functions, 
## such as noise removal and image enhancement. 
## Compare the effects of Laplacian and Gaussian filters on an image for different kernel windows.

## This image Download imagecontains Gaussian noise. In OpenCV, write algorithms for this image to do the following:

* Apply a Gaussian, a Laplacian, and a Gaussian with Laplacian filter using a 3x3 kernel. For Gaussian, think about how to select a good value of sigma for optimal results.
* Apply a Gaussian, a Laplacian, and a Gaussian with Laplacian filter using a 5x5 kernel. For gaussian, use the same value of sigma you selected in the above step.
* Apply a Gaussian, a Laplacian, and a Gaussian with Laplacian filter using a 7x7 kernel. For gaussian, use the same value of sigma you selected in the above step.
* Output your filter results as 3 x 3 side-by-side subplots to make comparisons easy to inspect visually. That is, your subplot should have 3 rows (1 for each kernel size) and 3 columns (1 for each filter type). Be sure to include row and column labels.

## Next, write a 2-3 page summary of your output results. Include in your summary, the following:

* Which filter type (Gaussian, Laplacian, or Gaussian with Laplacian) is preferred for better edge detection and why? 
> Provide two references of support for your answer and cite them in your summary using correct APA styling.

* Which filter (include kernel size and sigma, if applicable) performed the best visually? 
> Include details like whether there were image features better preserved and/or better enhanced. 
* Are these preservations and enhancements of image features important for edge detection? Why or why not?

* Are your results in line with the preferred method? Discuss why or why not?
> Your submission should be one executable Python script and one summary of 2-3 pages in length that conforms to CSU Global Writing Center. Include at least two scholarly references in addition to the course textbook. The CSU Global Library is a good place to find these references. The Writing Center and Library can be accessed by clicking on the tabs in the course navigation panel.