from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd


def predict(model, df):
    predictions_df = predict_model(estimator=model, data=df)
    return predictions_df['Label'][0]


st.set_page_config(
    layout="wide", page_icon='images/heineken1.jpeg',
    page_title='Heineken Brewery')

st.image('images/heineken_header.jpeg', use_column_width=True)

st.header("Beer Color Predictor for Heineken Brewery 🍻 ")

model = load_model('model/beer-color-pipeline2')


st.write('This is a web app to predict the Heineken beer color based on\
         several features that you can see in the sidebar. Please adjust the\
         value of each feature. After that, click on the Predict button at the bottom to\
         see the prediction of the regressor.')


def run():

    add_selectbox = st.sidebar.selectbox(
        "How would you like to predict?",
        ("Online", "Batch"))

    if add_selectbox == 'Online':

        roast_amount = st.sidebar.slider(label='Roast Amount (kg)', min_value=0,
                                         max_value=90,
                                         value=40,
                                         step=10)

        first_malt_amount = st.sidebar.slider(label='First Malt Amount (kg)', min_value=0,
                                              max_value=20000,
                                              value=13000,
                                              step=100)

        second_malt_amount = st.sidebar.slider(label='Second Malt Amount (kg)', min_value=0,
                                               max_value=10000,
                                               value=6000,
                                               step=100)

        mt_temperature = st.sidebar.slider(label='Malt cooker’s aggregated temperature', min_value=0,
                                           max_value=180,
                                           value=60,
                                           step=100)

        mt_time = st.sidebar.slider(label='Period of time that the batch stayed on malt cooker', min_value=0,
                                    max_value=12000,
                                    value=6700,
                                    step=100)

        wk_temperature = st.sidebar.slider(label='Wort cooker’s aggregated temperature', min_value=0,
                                           max_value=180,
                                           value=100,
                                           step=1)

        wk_steam = st.sidebar.slider(label='Wort cooker’s aggregated steam amount', min_value=0,
                                     max_value=10000,
                                     value=6000,
                                     step=100)

        wk_time = st.sidebar.slider(label='Period of time that the batch stayed on wort cooker', min_value=0,
                                    max_value=20000,
                                    value=6000,
                                    step=100)

        ph = st.sidebar.slider(label='pH measured during cooling', min_value=0,
                               max_value=10,
                               value=7,
                               step=1)

        total_cold_wort = st.sidebar.slider(label='Total batch volume of cold wort after cooling', min_value=0,
                                            max_value=2000,
                                            value=900,
                                            step=100)

        extract = st.sidebar.slider(label='Aggregated extract measured during cooling', min_value=0,
                                    max_value=20,
                                    value=15,
                                    step=1)

        woc_time = st.sidebar.slider(label='Period of time that the batch stayed on Wort Cooler', min_value=0,
                                     max_value=20,
                                     value=15,
                                     step=1)

        whp_transfer_time = st.sidebar.slider(label='Aggregated extract measured during cooling', min_value=0,
                                              max_value=2000,
                                              value=3000,
                                              step=100)

        whp_rest_time = st.sidebar.slider(label='Whirlpool Rest Time', min_value=0,
                                          max_value=20,
                                          value=15,
                                          step=1)

        roast_color = st.sidebar.slider(label='Color of roast malt', min_value=0,
                                        max_value=1000,
                                        value=900,
                                        step=10)

        first_malt_color = st.sidebar.slider(label='Color of 1st malt', min_value=0,
                                             max_value=20,
                                             value=6,
                                             step=1)

        second_malt_color = st.sidebar.slider(label='Color of 2nd malt', min_value=0,
                                              max_value=20,
                                              value=6,
                                              step=1)

        features = {'roast_amount': roast_amount, 'first_malt_amount': first_malt_amount,
                    'second_malt_amount': second_malt_amount, 'mt_temperature': mt_temperature,
                    'mt_time': mt_time, 'wk_temperature': wk_temperature, 'woc_time': woc_time,
                    'wk_steam': wk_steam, 'wk_time': wk_time, 'whp_transfer_time': whp_transfer_time,
                    'ph': ph, 'total_cold_wort': total_cold_wort, 'extract': extract,
                    'whp_rest_time': whp_rest_time, 'roast_color': roast_color,
                    'first_malt_color': first_malt_color, 'second_malt_color': second_malt_color
                    }

        features_df = pd.DataFrame([features])

        st.table(features_df)

        if st.button('Predict'):

            prediction = predict(model, features_df)

            st.success(
                f'Based on feature values, the beer color is {prediction:.2f}')

    if add_selectbox == 'Batch':

        file_upload = st.file_uploader(
            "Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model, data=data)
            st.write(predictions)


if __name__ == '__main__':
    run()
