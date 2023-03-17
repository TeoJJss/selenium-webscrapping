This project is to extract results from SPM official website.  
Visit https://gvs.moe.gov.my/qr/ for details.  

<b>DO THIS FIRST</b>  
Input to the project should be an image of SPM certificate with a visible QR code.  
Add the image path and student's examination number (angka giliran) in main.py file.  
Supported file format of image: jpg, png, jpeg  

<b>PROCESS</b>  
The algorithm will look for QR code in the SPM certificate file.  
And then, the algorithm will proceed to the official website's URL that is obtained from the image file.  
Lastly, the algorithm will return the texts obtained from the website.  
We can add algorithm to classify the texts in the future.  

<b>COMMANDS</b>  
To run, please ensure to use Python 3.9 or above, and run the following commands:  
```
pip install -r requirements.txt  
python main.py
```