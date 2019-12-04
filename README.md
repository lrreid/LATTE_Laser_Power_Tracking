# LATTE Laser Power Tracking
 Python GUI for saving sets of laser power measurements and plotting the history of the measurements

Each day, a set of measurements are recorded when the LATTE laser is switched on. This GUI makes it easier to save the measurements into a text file.
This text file is then used to plot the history of the measurements which is used to closely monitor the performance of the laser and help inform decision making for when periods of maintenance should be undertaken. For instance if we can see that the pulse energy out of the regen is constant but the energy out of the multipass amplifier is falling each day then perhaps it is time to replace the Powerlite laser flashlamps.


**The UI**
The interface is a basic UI written in tkinter. A screen shot is shown below:


The current days date is automatically added to the "Date" box in the UI but can be changed by the user if a previous days data is to be added.

The interface has three buttons:
* Save - Saves the entered values of laser power and energy into the text file _LATTE_Laser_Power_History.txt_
* Plot - Plots the pule energy at the exit of the regenerative and multipass amplifiers for the last 30 days
* Exit - Closes the program

The _Save_ button can only be pressed once, after which the button grays out and cannot be pressed again. This is to prevent the same days data being saved multiple times in the text file which stores all the data. An example of this is shown below:

**plotting**
The _Plot_ button opens plots based on matplotlib and pyplot. Two separate subplots are shown on a single image, the left hand image shows the pulse energy from the regenerative amplifier with the target value of 2 mJ shown as a red dotted line. The right hand image shows the pulse energy at the exit of the multipass amplifier with each of the Powerlite pump lasers on individually as well as the "Full power" which is both Powerlite lasers pumping the multipass crystal.
An example plot with example (fake) data is shown below:
