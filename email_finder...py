import re
strr =  '''
Items: 0 Amount: BDT 0 in cart Checkout now!
TechshopBD	
Techshop BangladeshLogin / Register
HomeSupportSpecial OffersTutorialsMy AccountContact UsTraining CourseFAQShopping Guideline
Shop By Categories
 
Starter Kits
Burners/Programmers
 
Development Boards
 
Arduino
 
FPGA
 
Robotics
 
Computer & Accessories
 
GSM/GPS/GPRS
 
Wireless
 
 
Breakout Boards
 
Modules
Micro Controllers
 
Analog ICs
 
Digital ICs
 
Displays
 
Cables & Connectors
 
Components
 
Regulator
 
Switching Device
 
Miscellaneous
 
Audio
 
Sensors
 
 
Solar
E-Textile
 
Tools
 
 
Retired
Shop By Suppliers
Techshop Bangladesh
Pi Labs, Bangladesh 
SparkFun, USA
Adafruit, USA
Seeed Studio, China
Pololu, USA
DFRobot, China
Hobbyking, Hong Kong
Marketplace, Bangladesh
Waveshare Electronics, China
Search 
Products
 
 
Home>Contact Us
Contact Us

Techshopbd 
ARA Bhaban, 39, Kazi Nazrul Islam Avenue 
Karwan Bazar, Dhaka-1215 
Bangladesh 


We do not take phone or email orders. Please feel free to order online at any time! For problems with an order or shipment please email: customerservice@techshopbd.com. 

If you have an urgent inquiry you may also contact us directly at: +8801841110110 (No phone orders please!) 

For help with technical issues using the techshopbd website please email: feedback@techshopbd.com. or send your question to: technicalsupport@techshopbd.com. 

For PCB related issues ask at: pcb@techshopbd.com. 

Product Photos: techshopbd product photos may be used without permission for educational purposes (research papers, school projects, etc.). However, permission must be granted for commercial use and proper credit to techshopbd must be given. For inquiries about the use of our product photos or permission to use them, please contact: sourcing@techshopbd.com.

 Submit your message
Name*	
Email*	
Subject*	
For which department?*	

General
Your message*	
What is 4 PLUS 1?*	
Payment Methods
COD

bkash

VAT Registration NO.
19121041942

Useful Links
Home
Training Course
FAQ
Support
Shopping Guideline
PCB Order Guideline
Warranty and Replacement
Terms & Conditions
Privacy Policy
About Us
Contact Us
Find Us
About Us
Techshopbd is one sort of your constant helping hand on whom you can rely, with no doubt, for any technological support and related assistance. To be more precise, it is an online retail store that sells the electronic bits and pieces needed for a competent electronic project. We don't discriminate among the bits and pieces on their sizes and range of use. Everything, that has even a minimum use at the project, is also considered with equal significance.

Follow us on shukuralom1234@gmail.com
Copyright © 2012-13 Techshop Bangladesh. All rights reserved.
'''
gmai = re.findall(r'\w+@\S+\w', strr)

for i in gmai:
   print(f"Gmail : {i}")
