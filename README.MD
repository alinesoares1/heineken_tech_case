<img src="https://github.com/alinesoares1/heineken_tech_case/blob/master/assets/heinekenapp.png">

# Predicting Beer Color for Heineken Brewery

Beer brewing is not an exact process, many factors play a role in brewing high quality beer, and one of the key quality parameters is the **color**. Beer color can vary from brew to brew due to changes in the process, changes in the ingredients, and a variety of other factors that have impact on the beer color. For this reason, beer companies have master brewers who play a very important role in overseeing the process.

Currently, 7% of Heineken's beer brews do not satisfy the requirements to achieve the "perfect" range of yellow, which means that 7% of all brews needs to be remixed, taking up production capacity that could be used for other purposes.

For this reason, this project aims to generate a machine learning model that use some historical heineken brewering data to predict the beer color for Heineken Brewery.

**Project Structure**:
<pre>
├── .streamlit/
│   └── config.toml
├── data/
│   └── heineken_data.csv
├── images/
│   ├── brewing_process.png
│   ├── heineken1.jpeg
│   ├── heineken_header.jpeg
│   └── heinekenapp.png
├── model/
│   ├── beer-color-pipeline2.pkl
│   └── predicting_beer_color.ipynb
├── .gitignore
├── Dockerfile
├── README.MD
├── app.py
└── requirements.txt
<pre>
## Usage

Execute the streamlit app module using the Dockerfile.

```
usage: docker build -t heinekenapp


then: docker run -p 8501:8501 heinekenapp
```

## Train

See all the training steps **[here](https://github.com/alinesoares1/heineken_tech_case/blob/master/model/predicting_beer_color.ipynb)**.
