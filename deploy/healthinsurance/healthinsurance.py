import pickle
import pandas as pd

class HealthInsurance (object):
    
    def __init__(self):
        self.robust_scaler_age = pickle.load(open('parameter/robust_scaler_age.pkl', 'rb'))
        self.robust_scaler_annual = pickle.load(open('parameter/robust_scaler_annual.pkl', 'rb'))
        self.ordinal_encoder = pickle.load(open('parameter/ordinal_encoder.pkl', 'rb'))
        self.frequency_encoder_gender = pickle.load(open('parameter/frequency_encoder_gender.pkl', 'rb'))
        self.frequency_encoder_region = pickle.load(open('parameter/frequency_encoder_region.pkl', 'rb'))
        self.frequency_encoder_policy = pickle.load(open('parameter/frequency_encoder_policy.pkl', 'rb'))
        self.frequency_encoder_vintage = pickle.load(open('parameter/frequency_encoder_vintage.pkl', 'rb'))

    def data_cleaning(self, df1):
        # rename columns
        cols_new = ['id', 'gender', 'age', 'driving_license', 'region_code',
       'previously_insured', 'vehicle_age', 'vehicle_damage', 'annual_premium',
       'policy_sales_channel', 'vintage']

        df1.columns = cols_new
        
        return df1

    def feature_engineering(self, df2):
        cols_drop = ['id']
        df2 = df2.drop(cols_drop, axis=1)
        
        return df2


    def data_preparation(self, df3):
        
        df3['age'] = self.robust_scaler_age.transform(df3[['age']].values)
        
        df3['annual_premium'] = self.robust_scaler_annual.transform(df3[['annual_premium']].values)

        df3['vehicle_age'] = self.ordinal_encoder.transform(df3[['vehicle_age']].values)
        
        df3['vehicle_damage'] = df3['vehicle_damage'].apply(lambda x: 1 if  x == 'Yes' else 0)
        
        df3['gender'] = df3['gender'].map(self.frequency_encoder_gender)
        
        df3['region_code'] = df3['region_code'].map(self.frequency_encoder_region)
        
        df3['policy_sales_channel'] = df3['policy_sales_channel'].map(self.frequency_encoder_policy)
        
        df3['vintage'] = df3['vintage'].map(self.frequency_encoder_vintage)
        
        # feature selection
        cols_selected = ['annual_premium', 'vintage', 'age', 'region_code', 'vehicle_damage', 'previously_insured',
                 'policy_sales_channel']
        
        return df3[cols_selected]
    

    def get_prediction(self, model, original_data, test_data):
        # model prediction
        pred = model.predict_proba(test_data)
        proba_1d = pred[:, 1].tolist()
        
        # join prediction into original data
        original_data['score'] = proba_1d
        
        return original_data.to_json(orient='records', date_format='iso')
