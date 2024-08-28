# Prophet Forecasting Pipeline

`Prophet_Forecasting_Pipeline.ipynb` performs time series forecasting using Facebook's Prophet model on Careem's Quik Data. The notebook provides a step-by-step guide on loading data, preprocessing it, training the Prophet model, and making predictions.

## Notebook Contents

### 1. **Data Loading and Preprocessing**
   - This section covers how to load the time series data and preprocess it to be used with the Prophet model. To load data call process_data(time_window, data_dir), where time window is the time interval of processing the orders and data_dir is the directory where the raw data is.  Note that the data for each month should be in the following format: anon_quik_month_year.csv. This will clean the raw data and process it in the format required for training. The processed data should be produced in the same working directory with a name like this: quik_data_all_final_10_mins.csv.

### 2. **Model Training**
   - Here, the notebook guides you through training the Prophet model using the preprocessed data. It includes steps for setting hyperparameters and fitting the model. Currently, the model is trained on a 10 minute window for each merchant seperately. The optimized hyperparameters for each merchant is stored in a dictionary to avoid running for days.

### 3. **Forecasting**
   - After training, the notebook demonstrates how to generate future forecasts using the trained model.

### 4. **Evaluation and Visualization**
   - This section provides methods to evaluate the model's performance and visualize the forecast results against actual data. The results are stored in folder "results_10_mins", which has a plot representing the forecasting results against the actual results on that day. Additionally, the forecast data is stored in a sheet named "predicted_forecasts" that has the predictions for each merchant separately.

### 5. **Saving and Loading the Model**
   - Instructions on how to save the trained model and reload it for future use are provided.


## Setup

To run the notebook, you need to have Python installed on your machine along with the required dependencies.


## Usage

1. Open the notebook in Jupyter Notebook or JupyterLab:
    ```bash
    jupyter notebook Prophet_Forecasting_Pipeline.ipynb
    ```
2. Follow the instructions provided in the notebook to load your dataset, preprocess the data, train the model, and generate forecasts.

## Dependencies

Ensure that you have the following dependencies installed:

- Python 3.6 or later
- pandas
- numpy
- matplotlib
- seaborn
- prophet
- pickle
- pathlib

You can install these packages using the following command:

```bash
pip install pandas numpy matplotlib seaborn prophet
