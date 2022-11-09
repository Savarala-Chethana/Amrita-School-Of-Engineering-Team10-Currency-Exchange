import streamlit as st
import base64
import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

st.sidebar.image('1.jpg', use_column_width=True)
st.sidebar.title("Let's Get Started")

st.title('NTRS Currency Exchange')
st.set_option('deprecation.showPyplotGlobalUse', False)

Duration=st.sidebar.radio(
        "Select the Time Span 👉",
        key="visibility",
        options=["None","Weekly", "Monthly","Quaterly", "Yearly"],
    )

Base_Currency= st.sidebar.selectbox("Base Rate",("None","USD"))

df = pd.read_csv("C:\\Users\\SAVARALA CHETHANA\\jupiter_codes\\Currency_Conversion_Test_Data\\Exchange_Rate_Report_2022.csv")

list_of_currencies = list(df.columns)
list_of_currencies =[x.split()[len(x.split())-1][1:4] for x in list_of_currencies]
list_of_currencies = list_of_currencies[1:len(list_of_currencies)-1]
list_of_currencies.sort()

Selected_Currency= st.sidebar.selectbox("Select the Exchange Rate",list_of_currencies)

if Duration=="Weekly":
    st.write("Enter Date in the give format : [04-Apr-2022]")
    text_input = st.text_input("Enter Date 👇")
    dat=text_input[0:7]+text_input[9:]
    yr = text_input[7:11]

    if st.button("Plot"):
        data = pd.read_csv("C:\\Users\\SAVARALA CHETHANA\\jupiter_codes\\Currency_Conversion_Test_Data\\Exchange_Rate_Report_" + yr + ".csv")
        list_of_currencies = list(data.columns)
        currencies = [x.split()[len(x.split()) - 1][1:4] for x in list_of_currencies]
        currencies[0] = "Date"
        data.columns = currencies

        data.fillna(method='ffill', inplace=True)

        rates = data[['Date', Selected_Currency]]
        rates = rates.values.tolist()

        list1 = list(data[Selected_Currency])
        list2 = list(data["Date"])
        l = len(rates)
        new = []

        for k in rates:
            for k1 in k:
                if k1 == str(dat):
                    x = rates.index(k)

        for i in range(x, x + 7):
            new.append([list2[i], list1[i]])

        df = pd.DataFrame(new)
        df.columns = ["date", Selected_Currency]

        # Plot the data
        fig, ax = plt.subplots()
        ax.plot(df["date"], df[Selected_Currency])
        st.pyplot(fig)

        st.write("The Date on which rate is minimum is " + min(new)[0]+" and the rate is "+str(min(new)[1]))
        st.write("The Date on which rate is maximum is " + max(new)[0]+" and the rate is "+str(max(new)[1]))

if Duration=="Monthly":
    st.write("Enter Date in the give format : [04-Apr-2022]")
    text_input = st.text_input("Enter Date 👇")
    yr = text_input[7:11]

    if st.button("Plot"):
        data = pd.read_csv("C:\\Users\\SAVARALA CHETHANA\\jupiter_codes\\Currency_Conversion_Test_Data\\Exchange_Rate_Report_" + yr+ ".csv")
        mon = text_input[3:6]
        list_of_currencies = list(data.columns)
        currencies = [x.split()[len(x.split()) - 1][1:4] for x in list_of_currencies]
        currencies[0] = "Date"
        data.columns = currencies

        data.fillna(method='ffill', inplace=True)

        rates = data[['Date', Selected_Currency]]
        list1 = list(data[Selected_Currency])
        list2 = list(data["Date"])
        l = len(rates)
        new = []
        for i in range(0, l - 1):
            if mon in list2[i]:
                new.append([list2[i], list1[i]])

        df = pd.DataFrame(new)
        df.columns = ["date", Selected_Currency]

        # Plot the data
        fig, ax = plt.subplots()
        ax.plot(df["date"], df[Selected_Currency])
        st.pyplot(fig)

        st.write("The Date on which rate is minimum is " + min(new)[0]+" and the rate is "+str(min(new)[1]))
        st.write("The Date on which rate is maximum is " + max(new)[0]+" and the rate is "+str(max(new)[1]))

if Duration=="Quaterly":
    st.write("Enter Date in the give format : [04-Apr-2022]")
    text_input = st.text_input("Enter Date 👇")
    yr = text_input[7:11]

    if st.button("Plot"):
        data = pd.read_csv("C:\\Users\\SAVARALA CHETHANA\\jupiter_codes\\Currency_Conversion_Test_Data\\Exchange_Rate_Report_" + yr + ".csv")
        mon_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        mon = text_input[3:6]
        n_l = mon_list.index(mon)
        list_of_currencies = list(data.columns)
        currencies = [x.split()[len(x.split()) - 1][1:4] for x in list_of_currencies]
        currencies[0] = "Date"
        data.columns = currencies
        mon_list = mon_list[n_l:n_l + 3]

        data.fillna(method='ffill', inplace=True)

        rates = data[['Date', Selected_Currency]]
        list1 = list(data[Selected_Currency])
        list2 = list(data["Date"])
        l = len(rates)
        new = []
        for i in range(0, l - 1):
            for j in mon_list:
                if j in list2[i]:
                    new.append([list2[i], list1[i]])

        df = pd.DataFrame(new)
        df.columns = ["date", Selected_Currency]

        # Plot the data
        fig, ax = plt.subplots()
        ax.plot(df["date"], df[Selected_Currency])
        st.pyplot(fig)

        st.write("The Date on which rate is minimum is " + min(new)[0]+" and the rate is "+str(min(new)[1]))
        st.write("The Date on which rate is maximum is " + max(new)[0]+" and the rate is "+str(max(new)[1]))

if Duration=="Yearly":
    st.write("Enter Year in the given format: [2022]")
    text_input = st.text_input("Enter Year 👇")

    if st.button("Plot"):
        data = pd.read_csv("C:\\Users\\SAVARALA CHETHANA\\jupiter_codes\\Currency_Conversion_Test_Data\\Exchange_Rate_Report_" + text_input + ".csv")
        list_of_currencies = list(data.columns)
        currencies = [x.split()[len(x.split()) - 1][1:4] for x in list_of_currencies]
        currencies[0] = "Date"
        data.columns = currencies

        data.fillna(method='ffill', inplace=True)

        list1 = list(data[Selected_Currency])
        list2 = list(data["Date"])
        l = len(list1)
        rates = []

        for i in range(0, l - 1):
            rates.append([list2[i], list1[i]])
        print(rates)

        df = pd.DataFrame(rates)
        df.columns = ["date", Selected_Currency]

        # Plot the data
        fig, ax = plt.subplots()
        ax.plot(df["date"], df[Selected_Currency])
        st.pyplot(fig)

        st.write("The Date on which rate is minimum is "+min(rates)[0]+" and the rate is "+str(min(rates)[1]))
        st.write("The Date on which rate is maximum is "+max(rates)[0]+" and the rate is "+str(max(rates)[1]))


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('5.jpg')




