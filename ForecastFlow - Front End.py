from tkinter import *
from PIL import Image, ImageTk

root= Tk()

width= 800
height= 400
root.geometry(f"{width}x{height}")


# Importing Model
import joblib
model= joblib.load('model.pkl')

def result():
    #for locations
    loc_map = {
    'Portland': 1,
    'Sydney': 2,
    'Cairns': 3,
    'Albany': 4,
    'Darwin': 5,
    'MountGambier': 6,
    'Dartmoor': 7,
    'NorfolkIsland': 8,
    'CoffsHarbour': 9,
    'Walpole': 10,
    'Witchcliffe': 11,
    'Hobart': 12,
    'NorahHead': 13,
    'GoldCoast': 14,
    'Canberra': 15,
    'Ballarat': 16,
    'SydneyAirport': 17,
    'Brisbane': 18,
    'Adelaide': 19,
    'MountGinini': 20,
    'Launceston': 21,
    'Watsonia': 22,
    'Perth': 23,
    'Wollongong': 24,
    'Sale': 25,
    'Newcastle': 26,
    'Albury': 27,
    'BadgerysCreek': 28,
    'Nuriootpa': 29,
    'MelbourneAirport': 30,
    'Tuggeranong': 31,
    'Penrith': 32,
    'PerthAirport': 33,
    'Bendigo': 34,
    'Richmond': 35,
    'Williamtown': 36,
    'WaggaWagga': 37,
    'SalmonGums': 38,
    'Townsville': 39,
    'Cobar': 40,
    'Melbourne': 41,
    'PearceRAAF': 42,
    'Moree': 43,
    "Mildura": 44,
    "AliceSprings": 45,
    "Woomera": 46,
    "Nhil": 47,
    "Katherine": 48,
    "Uluru": 49
    }
    loc= loc_map.get(value.get())
    print(loc)

    #for month
    month_map =  {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
    }
    month= month_map.get(value2.get())
    print(month)

    #for Rain_today
    rtoday_map= {
        "Yes": 1,
        "No": 0
    }
    rtoday=  rtoday_map.get(value1.get())
    print(rtoday)

    #Direction
    dir_map={
    'W': 4,
    'SE': 23,
    'E': 3,
    'N': 1,
    'SSE': 223,
    'S': 2,
    'WSW': 424,
    'SW': 24,
    'SSW': 224,
    'WNW': 414,
    'NW': 14,
    'ENE': 313,
    'ESE': 323,
    'NE': 13,
    'NNW': 114,
    'NNE': 113
    }
    dir_gust= dir_map.get(v15.get())
    print(dir_gust)
    dir_9am= dir_map.get(v16.get())
    print(dir_9am)
    dir_3pm= dir_map.get(v16.get())
    print(dir_3pm)



    data= [v1.get(), v2.get(), v3.get(), v4.get(), v5.get(), v6.get(), v7.get(), v8.get(), v9.get(), v10.get(), v11.get(), v12.get(), v13.get(), v14.get(), month, loc, dir_gust, dir_9am, dir_3pm, rtoday]
    data = [float(item) for item in data]    
    print(data)
    tomorrow_rain= model.predict([data])

    probabilities = model.predict_proba([data])
    percentage = probabilities[0][1] * 100
    percentage= '{:.2f}'.format(percentage)
    print(percentage)

    if tomorrow_rain == 1:
        tomorrow_rain="YES"
    elif tomorrow_rain == 0:
        tomorrow_rain="NO"
    print(tomorrow_rain)

    f3= Frame(root, borderwidth= 7, relief= SUNKEN)
    f3.pack(anchor= "s", side= BOTTOM, padx= 45)
    if tomorrow_rain == "YES":
        result= Label(f3, text= tomorrow_rain.upper(), font=("Times New Roman", 55, "bold"), fg="green")
        result.grid(row= 4)
        result2= Label(f3, text= "Chances of Rainfall Tomorrow: "+percentage+'%', font=("Times New Roman", 20, "bold"))
        result2.grid(row= 5)
    elif tomorrow_rain == "NO":
        result= Label(f3, text= tomorrow_rain.upper(), font=("Times New Roman", 55, "bold"), fg="red")
        result.grid(row= 4)
        result2= Label(f3, text= "Chances of Rainfall Tomorrow: "+percentage+'%', font=("Times New Roman", 20, "bold"))
        result2.grid(row= 5)

        


root.title("ForecastFlow")
root.iconbitmap('images/logo.ico')

# Load the background image
background_image = Image.open("images/rain_drops.png")
background_image = ImageTk.PhotoImage(background_image)

#Create a Label to display the background image and place it in the window
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

f1 = Frame(root, bg="lavender", borderwidth=5, relief=RIDGE)
f1.pack(side=TOP)

logo_open= Image.open("images/logo.png")
size= (150,150)
logo_resize= logo_open.resize(size)
logo= ImageTk.PhotoImage(logo_resize)
logo_png= Label(f1, image=logo, bg= "lavender")
# pack the logo label with side='left'
logo_png.pack(side='left', anchor='n', fill=X)

heading= Label(f1,text="ForecastFlow: Rainfall Prediction System",fg="Navy" , font=("Comic Sans MS", 28, "bold"), bg= "lavender")
# pack the heading label with side='right'
heading.pack(side='top', anchor='n', pady=42, padx=20)

f2= Frame(root)
f2.pack(anchor= "n", side=TOP)

#Location
location= Label(f2, text= "Location: ", font=("Times New Roman", 14, "bold"))
location.grid(row=0, column=1, pady= 40)

value= StringVar()
location_options= ["Select", "Adelaide", "Albany", "AliceSprings", "Albury", "BadgerysCreek", "Ballarat", "Bendigo", "Brisbane", "Cairns", "Cobar", "CoffsHarbour", "Dartmoor", "Darwin", "GoldCoast", "Hobart", "Katherine", "Launceston", "Melbourne", "MelbourneAirport", "Mildura", "Moree", "MountGambier", "MountGinini", "Newcastle", "Nhil", "NorfolkIsland", "NorahHead", "Nuriootpa", "PearceRAAF", "Penrith", "Perth", "PerthAirport", "Portland", "Richmond", "Sale", "SalmonGums", "Sydney", "SydneyAirport", "Townsville", "Tuggeranong", "Uluru", "Walpole", "Wollongong", "Woomera", "Watsonia", "Williamtown", "WaggaWagga", "Witchcliffe"]
location_entry= OptionMenu(f2, value , *location_options)
location_entry.grid(row=0, column=2)
value.set(location_options[0])

#MinTemp
MinTemp= Label(f2, text= "MinTemp: ", font=("Times New Roman", 14))
MinTemp.grid(row=2, column=1, padx= 20)
v1= StringVar()
MinTemp_v1= Entry(f2, textvariable= v1)
MinTemp_v1.grid(row=2, column=2)

#MaxTemp
MaxTemp= Label(f2, text= "MaxTemp: ", font=("Times New Roman", 14))
MaxTemp.grid(row=3, column=1, padx= 20)
v2= StringVar()
MaxTemp_v2= Entry(f2, textvariable= v2)
MaxTemp_v2.grid(row=3, column=2)

#Rainfall
Rainfall= Label(f2, text= "Rainfall: ", font=("Times New Roman", 14))
Rainfall.grid(row=4, column=1, padx= 20)
v3= StringVar()
Rainfall_v3= Entry(f2, textvariable= v3)
Rainfall_v3.grid(row=4, column=2)

#WindGustSpeed
WindGustSpeed= Label(f2, text= "WindGustSpeed: ", font=("Times New Roman", 14))
WindGustSpeed.grid(row=5, column=1, padx= 20)
v4= StringVar()
WindGustSpeedv4= Entry(f2, textvariable= v4)
WindGustSpeedv4.grid(row=5, column=2)

#WindSpeed9am
WindSpeed9am= Label(f2, text= "WindSpeed9am: ", font=("Times New Roman", 14))
WindSpeed9am.grid(row=6, column=1)
v5= StringVar()
WindSpeed9amv5= Entry(f2, textvariable= v5)
WindSpeed9amv5.grid(row=6, column=2)

#WindSpeed3pm
WindSpeed3pm= Label(f2, text= "WindSpeed3pm: ", font=("Times New Roman", 14))
WindSpeed3pm.grid(row=7, column=1)
v6= StringVar()
WindSpeed3pmv6= Entry(f2, textvariable= v6)
WindSpeed3pmv6.grid(row=7, column=2)

#Humidity9am
Humidity9am= Label(f2, text= "Humidity9am: ", font=("Times New Roman", 14))
Humidity9am.grid(row=2, column=3, padx= 20)
v7= StringVar()
Humidity9amv7= Entry(f2, textvariable= v7)
Humidity9amv7.grid(row=2, column=4)

#Humidity3pm
Humidity3pm= Label(f2, text= "Humidity3pm: ", font=("Times New Roman", 14))
Humidity3pm.grid(row=3, column=3, padx= 20)
v8= StringVar()
Humidity3pmv8= Entry(f2, textvariable= v8)
Humidity3pmv8.grid(row=3, column=4)

#Pressure9am
Pressure9am= Label(f2, text= "Pressure9am: ", font=("Times New Roman", 14))
Pressure9am.grid(row=4, column=3, padx= 20)
v9= StringVar()
Pressure9amv9= Entry(f2, textvariable= v9)
Pressure9amv9.grid(row=4, column=4)

#Pressure3pm
Pressure3pm= Label(f2, text= "Pressure3pm: ", font=("Times New Roman", 14))
Pressure3pm.grid(row=5, column=3, padx= 20)
v10= StringVar()
Pressure3pmv10= Entry(f2, textvariable= v10)
Pressure3pmv10.grid(row=5, column=4)

#Cloud9am
Cloud9am= Label(f2, text= "Cloud9am: ", font=("Times New Roman", 14))
Cloud9am.grid(row=6, column=3, padx= 20)
v11= StringVar()
Cloud9amv11= Entry(f2, textvariable= v11)
Cloud9amv11.grid(row=6, column=4)

#Cloud3pm
Cloud3pm= Label(f2, text= "Cloud3pm: ", font=("Times New Roman", 14))
Cloud3pm.grid(row=7, column=3, padx= 20)
v12= StringVar()
Cloud3pmv12= Entry(f2, textvariable= v12)
Cloud3pmv12.grid(row=7, column=4)

#Temp9am
Temp9am= Label(f2, text= "Temp9am: ", font=("Times New Roman", 14))
Temp9am.grid(row=2, column=5, padx= 20)
v13= StringVar()
Temp9amv13= Entry(f2, textvariable= v13)
Temp9amv13.grid(row=2, column=6)

#Temp3pm
Temp3pm= Label(f2, text= "Temp3pm: ", font=("Times New Roman", 14))
Temp3pm.grid(row=3, column=5, padx= 20)
v14= StringVar()
Temp3pmv14= Entry(f2, textvariable= v14)
Temp3pmv14.grid(row=3, column=6)

#WindGustDir
WindGustDir= Label(f2, text= "WindGustDir: ", font=("Times New Roman", 14))
WindGustDir.grid(row=4, column=5, padx= 20)
v15= StringVar()
WindGustDirv15= Entry(f2, textvariable= v15)
WindGustDirv15.grid(row=4, column=6)

#WindDir9am
WindDir9am= Label(f2, text= "WindDir9am: ", font=("Times New Roman", 14))
WindDir9am.grid(row=5, column=5, padx= 20)
v16= StringVar()
WindDir9amv16= Entry(f2, textvariable= v16)
WindDir9amv16.grid(row=5, column=6)

#WindDir3pm
WindDir3pm= Label(f2, text= "WindDir3pm: ", font=("Times New Roman", 14))
WindDir3pm.grid(row=6, column=5, padx= 20)
v17= StringVar()
WindDir3pmv17= Entry(f2, textvariable= v17)
WindDir3pmv17.grid(row=6, column=6)

#RainToday
RainToday= Label(f2, text= "RainToday: ", font=("Times New Roman", 14))
RainToday.grid(row=0, column=3, pady= 20)

value1= StringVar()
RainToday_options= ["Select","Yes","No"]
RainToday_entry= OptionMenu(f2, value1 , *RainToday_options)
RainToday_entry.grid(row=0, column=4)
value1.set(RainToday_options[0])

#Month
Month= Label(f2, text= "Month: ", font=("Times New Roman", 14))
Month.grid(row=0, column=5, pady= 20)

value2= StringVar()
month_options= ["Select","January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
Month_entry= OptionMenu(f2, value2 , *month_options)
Month_entry.grid(row=0, column=6)
value2.set(month_options[0])

b1= Button(f2, text= "PREDICT!", fg="red", font=("Times New Roman", 14), bg="black", command= result)
b1.grid(row=9, column=4, pady= 20)

#credit= Label(root, text= "Project Team:\nAl Saim Shakeel\nAhtisham riyasat\nSupervised by: Mr. Aftaab Alam")
#credit.pack(anchor='s', side= "right")
f_credit= Frame(root, borderwidth=5, relief= SUNKEN)
f_credit.pack(anchor="s", side= LEFT)
credit= Label(f_credit, text="Developed By:", font=("Times New Roman", 14, "bold", "underline"))
credit.grid(row=3, pady= 10)
credit_n1= Label(f_credit, text="Al Saim Shakeel (Leader)", font=("Times New Roman", 12, "italic", 'bold'))
credit_n1.grid(row=4)
credit_n1= Label(f_credit, text="Ahtisham Riyasat", font=("Times New Roman", 12, "italic", 'bold'))
credit_n1.grid(row=5)
credit_s= Label(f_credit, text="Supervised By: Mr. Aaftab Alam", font=("Times New Roman", 12, "italic", 'bold'))
credit_s.grid(row=6)



root.mainloop()
