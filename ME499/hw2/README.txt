****************************************************
ME 499 Computer Programming for Mechanical Systems
      	Code by Samuel J. Stumbo
             	Homework #6
  	     	26 May 2018

****************************************************

filename: hw2.py

Comments:
Part 1 - Use m = MUCamera()
	and then m.average_intensity() to return the average intensity of a single pic
	from the MU camera.

Part 2 - I was not able to get my filtered image to work very quickly. It took 20-30 seconds
	to process each image. I did not even try to plot the values from this.

Part 3 - Hmm... The once a second thing didn't work. I defaulted to 6 seconds, but
	even then, the picture would stay the same for several of these data points. For 
	this part I used a separate function outside my class that called an instance of the class
	The plot that I generated was noisy. It was generated late at night because I
	screwed up and was not able to plot values from the previous two nights ( I 
	saved images to access the first night and the second night I saved the PIL instance.
	I thought it would be easy to access these, but It was not... I'll try again, but 
	the included plot taken over a ten minute time is the best I have

Part 4 - I put my code in a class like you asked

Part 5 - I set a threshold of 70 for the intensity value that triggered night time. This works
	fine and can be called with m.daytime()

Part 6 - I wrote code for this based on something I found on stack exchange -
	I think it's working but it is taking a ridiculous amount of time to run. 
	There must be a better way!!!
Answers:

What is the most common (r, g, b) tuple?

What color is this?

What proportion of pixels have this color?


All the rest is code that didn't make the cut, but that I used in some capacity and 
would like to use again.  
*******************************************************************************

        # for pixel in rgb:
        #     ave_rgb.append(np.average(pixel))
        # ave_int = np.average(ave_rgb)

        # images = []
        # t = time.time()

        # while time.time() - t < how_long:
        #     interval = time.time() - last_time
        #     if interval >= 6:
        #         print('COMPUTING')
        #         cnt += 1
        #         images.append(w.grab_image())
        #
        #         last_time = time.time()
        # with open('images_5_31.csv', 'w') as csvfile:
        #     writer = csv.writer(csvfile)
        #     writer.writerow(images)
        # csvfile.close()
        #ave_int = []

        # for im in images:
        #     rgb = im.getdata()
        #     ave_rgb = []
        #     for pixel in rgb:
        #         ave_rgb.append(np.average(pixel))
        #     ave_int = np.average(ave_rgb)
            #print('Thinking')
            #average_intensity.append(np.average(ave_rgb))