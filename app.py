#!/usr/bin/env python
# coding: utf-8

# # Making a web application with the streamlit framework

# In[1]:


from pycaret.classification import load_model, predict_model 
import pandas as pd 
import numpy as np
import streamlit as st
from PIL import Image
import os


# In[2]:


class StreamlitApp:
    
    def __init__(self):
        self.model = load_model('model') 
        #Defining the csv path
        self.save_fn = 'path.csv'     
        
    def predict(self, input_data): 
        return predict_model(self.model, data=input_data)
    
    def store_prediction(self, output_df): 
        if os.path.exists(self.save_fn):
            save_df = pd.read_csv(self.save_fn)
            save_df = save_df.append(output_df, ignore_index=True)
            save_df.to_csv(self.save_fn, index=False)
            
        else: 
            output_df.to_csv(self.save_fn, index=False)  
            
    
    def run(self):
        #Puts an image to application
        image = Image.open('house_prices.gif')
        st.image(image, use_column_width=False)
    
    
        st.sidebar.info('This app is created to predict house prices' )
        st.sidebar.success('DAT158')
        st.title('House Prices Prediction')
        
       
        #features defined in csv file
        MSSubClass = st.number_input('MSSubClass', min_value=10, max_value=1000, value=60)
        MSZoning = st.selectbox('MSZonning', ['RH', 'RL', 'RM', 'FV'])
        LotFrontage = st.slider('LotFrontage',min_value=0, max_value=150, value=60, step=1)
        LotArea = st.number_input('LotArea', min_value=0, max_value=100000, value=10000)
        Street = st.selectbox('Street', ['Pave', 'Grvl'])
        Alley = st.selectbox('Alley', ['Pave', 'Grvl'])
        LotShape = st.selectbox('LotShape', ['Reg', 'IR1'])
        LandContour = st.selectbox('LandContour', ['Lvl', 'HLS', 'Bnk'])
        Utilities = st.selectbox('Utilities', ['AllPub', 'HLS', 'Bnk'])
        LotConfig = st.selectbox('LotConfig', ['Inside', 'Corner', 'FR2'])
        LandSlope = st.selectbox('LandSlope', ['Gtl', 'Mod'])
        Neighborhood = st.selectbox('Neighborhood', ['NAmes', 'Gilbert','StoneBr'])
        Condition1 = st.selectbox('Condition1', ['Feedr', 'Norm','PosN'])
        Condition2 = st.selectbox('Condition2', ['Feedr', 'Norm','PosN'])
        BldgType = st.selectbox('BldgType', ['1Fam', 'TwnhsE','Twnhs'])
        HouseStyle = st.selectbox('HouseStyle', ['1Story', '2Story','SLvl','1.5Fin'])
        OverallQual = st.slider('OverallQual',min_value=0, max_value=10, value=5, step=1)
        OverallCond = st.slider('OverallCond',min_value=0, max_value=10, value=5, step=1)


        YearBuilt = st.slider('YearBuilt',min_value=1900, max_value=2021, value=2000, step=1)
        YearRemodAdd = st.slider('YearRemodAdd',min_value=1900, max_value=2021, value=2000, step=1)
        RoofStyle = st.selectbox('RoofStyle', ['Gable', 'Hip'])
        RoofMatl = st.selectbox('RoofMatl', ['CompShg', 'Tar&Grv'])
        Exterior1st = st.selectbox('Exterior1st', ['VinylSd', 'Wd Sdng','HdBoard'])
        Exterior2nd = st.selectbox('Exterior2nd', ['VinylSd', 'Wd Sdng','HdBoard'])
        MasVnrType = st.selectbox('MasVnrType', ['BrkFace', 'Stone'])
        MasVnrArea = st.number_input('MSSubClass', min_value=0, max_value=10000, value=300)
        ExterQual = st.selectbox('ExterQual', ['Ta', 'Gd','Ex'])
        ExterCond = st.selectbox('ExterCond', ['Ta', 'Gd','Ex'])
        Foundation = st.selectbox('Foundation', ['CBlock', 'PConc'])
        BsmtQual = st.selectbox('BsmtQual', ['Ta', 'Gd','Ex'])
        BsmtCond = st.selectbox('BsmtCond', ['Ta', 'Gd','Ex'])
        BsmtExposure = st.selectbox('BsmtExposure', ['No', 'Gd','Av'])
        BsmtFinType1 = st.selectbox('BsmtFinType1', ['Rec', 'ALQ','GLQ'])
        BsmtFinSF1 = st.number_input('BsmtFinSF1', min_value=0, max_value=10000, value=300)
        BsmtFinType2 = st.selectbox('BsmtFinType2', ['LwQ', 'Unf','Rec','BLQ'])

        BsmtFinSF2 = st.number_input('BsmtFinSF2', min_value=0, max_value=10000, value=300)
        BsmtUnfSF = st.number_input('BsmtUnfSF', min_value=0, max_value=10000, value=300)
        TotalBsmtSF = st.number_input('TotalBsmtSF', min_value=0, max_value=10000, value=300)
        Heating = st.selectbox('Heating', ['GasA', 'GasW'])
        HeatingQC = st.selectbox('HeatingQC', ['Ta', 'Gd','Ex'])
        CentralAir = st.selectbox('CentralAir', ['Y', 'N'])
        Electrical = st.selectbox('Electrical', ['FuseA', 'SBrkr'])
        fistFlrSF = st.number_input('1stFlrSF', min_value=0, max_value=10000, value=300)
        sendFlrSF = st.number_input('2ndFlrSF', min_value=0, max_value=10000, value=300)
        LowQualFinSF = st.number_input('LowQualFinSF', min_value=0, max_value=10000, value=300)
        GrLivArea = st.number_input('GrLivArea', min_value=0, max_value=10000, value=300)
        BsmtFullBath = st.number_input('BsmtFullBath', min_value=0, max_value=10000, value=300)
        BsmtHalfBath = st.number_input('BsmtHalfBath', min_value=0, max_value=10000, value=300)
        FullBath = st.number_input('FullBath', min_value=0, max_value=10000, value=300)
        HalfBath = st.number_input('HalfBath', min_value=0, max_value=10000, value=300)
        BedroomAbvGr = st.number_input('BedroomAbvGr', min_value=0, max_value=10000, value=300)
        KitchenAbvGr = st.number_input('KitchenAbvGr', min_value=0, max_value=10000, value=300)

        KitchenQual = st.selectbox('KitchenQual', ['Ta', 'Gd','Ex'])
        TotRmsAbvGrd = st.slider('TotRmsAbvGrd',min_value=0, max_value=30, value=5, step=1)
        Functional = st.selectbox('Functional', ['Typ', 'Min1','Min2'])
        Fireplaces = st.slider('Fireplaces',min_value=0, max_value=10, value=0, step=1)
        FireplaceQu = st.selectbox('FireplaceQu', ['NA','Ta', 'Gd','Ex'])
        GarageType = st.selectbox('GarageType', ['Attchd', 'Detchd','Ex'])
        GarageYrBlt = st.number_input('GarageYrBlt', min_value=1900, max_value=2021, value=2000)
        GarageFinish = st.number_input('GarageFinish', min_value=1900, max_value=2021, value=2000)
        GarageCars = st.slider('GarageCars',min_value=0, max_value=10, value=1, step=1)
        GarageArea = st.number_input('GarageArea', min_value=0, max_value=10000, value=600)
        GarageQual = st.selectbox('GarageQual', ['TA', 'NA','Fa'])
        GarageCond = st.selectbox('GarageCond', ['TA', 'NA','Fa'])
        PavedDrive = st.selectbox('PavedDrive', ['Y', 'N','P'])
        WoodDeckSF = st.number_input('WoodDeckSF', min_value=0, max_value=1000, value=100)
        OpenPorchSF = st.number_input('OpenPorchSF', min_value=0, max_value=1000, value=100)
        EnclosedPorch = st.number_input('EnclosedPorch', min_value=0, max_value=1000, value=100)
        ThreeSsnPorch = st.number_input('ThreeSsnPorch', min_value=0, max_value=1000, value=100)
        ScreenPorch = st.number_input('ScreenPorch', min_value=0, max_value=1000, value=100)
        PoolArea = st.number_input('PoolArea', min_value=0, max_value=1000, value=100)
        PoolQC = st.selectbox('PoolQC', ['NA', 'Gd'])
        Fence = st.selectbox('Fence', ['MnPrv', 'NA','GdPrv'])
        MiscFeature = st.selectbox('MiscFeature', ['NA', 'Gar2','Shed'])
        MiscVal = st.number_input('MiscVal', min_value=0, max_value=100000, value=0)

        MoSold = st.slider('MoSold',min_value=0, max_value=10, value=0, step=1)
        YrSold = st.number_input('YrSold', min_value=1900, max_value=2021, value=2010)
        SaleType = st.selectbox('SaleType', ['WD', 'COD','New'])
        SaleCondition = st.selectbox('SaleCondition', ['Normal', 'Abnorml','Partial'])

        output = ''
        input_dict = {'MSSubClass':MSSubClass,'MSZoning':MSZoning,'LotFrontage':LotFrontage,'LotArea':LotArea,'Street':Street,'Alley':Alley,'LotShape':LotShape,'LandContour':LandContour,'Utilities':Utilities,'LotConfig':LotConfig,'LandSlope':LandSlope,'Neighborhood':Neighborhood,'Condition1':Condition1,'Condition2':Condition2,'BldgType':BldgType,'HouseStyle':HouseStyle,'OverallQual':OverallQual,'OverallCond':OverallCond,'YearBuilt':YearBuilt,'YearRemodAdd':YearRemodAdd,'RoofStyle':RoofStyle,'RoofMatl':RoofMatl,'Exterior1st':Exterior1st,'Exterior2nd':Exterior2nd, 'MasVnrType':MasVnrType,'MasVnrArea':MasVnrArea,'ExterQual':ExterQual,'ExterCond':ExterCond,'Foundation':Foundation,'BsmtQual':BsmtQual,'BsmtCond':BsmtCond,'BsmtExposure':BsmtExposure,'BsmtFinType1':BsmtFinType1,'BsmtFinSF1':BsmtFinSF1,'BsmtFinType2':BsmtFinType2,'BsmtFinSF2':BsmtFinSF2,'BsmtUnfSF':BsmtUnfSF,'TotalBsmtSF':TotalBsmtSF,'Heating':Heating,'HeatingQC':HeatingQC,'CentralAir':CentralAir,'Electrical':Electrical,'1stFlrSF':fistFlrSF,'2ndFlrSF':sendFlrSF,'LowQualFinSF':LowQualFinSF,'GrLivArea':GrLivArea,'BsmtFullBath':BsmtFullBath,'BsmtHalfBath':BsmtHalfBath,'FullBath':FullBath,'HalfBath':HalfBath,'BedroomAbvGr':BedroomAbvGr,'KitchenAbvGr':KitchenAbvGr,'KitchenQual':KitchenQual,'TotRmsAbvGrd':TotRmsAbvGrd,'Functional':Functional,'Fireplaces':Fireplaces,'FireplaceQu':FireplaceQu,'GarageType':GarageType,'GarageYrBlt':GarageYrBlt,'GarageFinish':GarageFinish,'GarageCars':GarageCars,'GarageArea':GarageArea,'GarageQual':GarageQual,'GarageCond':GarageCond,'PavedDrive':PavedDrive,'WoodDeckSF':WoodDeckSF,'OpenPorchSF':OpenPorchSF,'EnclosedPorch':EnclosedPorch,'3SsnPorch':ThreeSsnPorch,'ScreenPorch':ScreenPorch,'PoolArea':PoolArea,'PoolQC':PoolQC,'Fence':Fence,'MiscFeature':MiscFeature,'MiscVal':MiscVal,'MoSold':MoSold,'YrSold':YrSold,'SaleType':SaleType,'SaleCondition':SaleCondition}



        input_df = pd.DataFrame(input_dict,index=[0])

        if st.button('Predict'): 
            output = self.predict(input_df)
            self.store_prediction(output)

        st.success('Predicted output: {}'.format(output))
            
sa = StreamlitApp()
sa.run()





