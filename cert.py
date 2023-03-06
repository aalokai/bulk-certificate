import openpyxl
import cv2
list_names=['Aalok Tiwari',
'Aanshi Srivastava',
'Aastha Seth',
'Abhinav Chaurasia',
'Abhishek Chaurasiya',
'Abhishek Pandey',
'Abhishek Pratap Singh',
'Abhishek Yadav',
'Adarsh Keshrwani',
'Adarsh Mishra',
'Adarsh Tripathi',
'Aditi Kanaujiya',
'Aditi Mishra',
'Ajeet Singh',
'Akash Agarwal',
'Akshat Giri'
,'Aman Maurya'
,'Aman Singh'
,'Ananya Verma'
,'Angel Praveen'
,'Ankit Gangwar'
,'Ankit Kumar.'
,'Ankit Pal Dhangar'
,'Anubhav Tiwari'
,'Anurag Gupta'
,'Arvind Srivastav'
,'Ashish Suryavanshi'
,'Ashutosh Tiwari'
,'Atul Baliyan'
,'Ayush Tiwari'
,'Bhanu Pratap'
,'Brawl Stars Studio'
,'Brijesh Kumar'
,'Chirag Garg'
,'Chirag Purwar'
,'Corpse'
,'DIPTI RAI'
,'Dev Prakash Rai'
,'Diksha'
,'Dipendra Dikshit'
,'Farhan'
,'Harsh Sharma'
,'Harshit Singh'
,'Himanshu Gupta'
,'Kanha'
,'Kaushik Sharma'
,'Kishan Sharma'
,'MOHD WAZEH'
,'Mahi Srivastava'
,'Manju Gupta'
,'Mayank Dhar Pandey'
,'Md Aquib khan'
,'Mohammad Abbas'
,'Mr Asmit'
,'Mritunjay Dwivedi'
,'Niightout'
,'Nisha Yadav'
,'Paritosh Vatsal Tripathi'
,'Pratyush Srivastava'
,'Premlata Kumari'
,'Rahul Prajapati'
,'Rahul Srivastava'
,'Ravi yadav'
,'SUPRIYA YADAV'
,'Sakshi Kashyap'
,'Sakshi Srivastava'
,'Saurabh kumar'
,'Shipra Tripathi'
,'Shyam Patel'
,'Siddharth Shukla'
,'Sundaram Tiwari'
,'Tarun Agarwal'
,'Udit Chand Narayan'
,'Ujjawal Rastogi'
,'Vikas'
,'Vikas Kashyap'
,'Yogendra Srivastava'
,'Yuvraj Sachan'
,'Zeeshan Ahmad'
,'Akash Tiwari'
,'Aryama Pandey'
,'Asingh Singh'
,'Himanshu Pandey'
,'Jai Mehrotra']

for index, name in enumerate(list_names):
    template = cv2.imread('webc.png')
    cv2.putText(template,name,(2200,2180),cv2.FONT_HERSHEY_COMPLEX, 7,(0,0,0),10,cv2.LINE_AA)
    cv2.imwrite(f'/home/aalok/Aalok/IC/inspire to innovate/certi/webce/{name}.png',template)
    print('Processing Certificate {}/{}'.format(index+1,len(list_names)))
    