# ModelBehaviour
# Data analytics class project 2019
# Costa Rican Household Poverty Level Prediction

## Problem Statement
Classficiation of households based on poverty level for allocation of welfare benifits and reporting information regarding proimenent features that cause households to fall in these categories to enable upliftment.

## Short description of the project
This project focuses on prediction of poverty levels of households based on socio-economic factors and classifies them into 4 distinct categories. Features selection and level classification on a data set containing household characteristics of a representative sample of Costa Rican households allows accurate insights into features to enable local development in the required areas and appropriate allotment of funds for social welfare benefits.

## Description of files
PCA: contains PCA_trian.Rmd(to analyse the variances and graphs in detail), PCA_analysis.ipynb( Using PCA for modelling)<br />
RawData: contains test.csv and train.csv<br /> 
version_1_preprocess.Rmd: R markdown file used for data cleaning and preprocessing. It contains 2 output csv files.<br /> 
EDA.Rmd: R Markdown file that contains preliminary EDA on the preprocessed data and exploratory analysis using visualization.<br /> 
EDA_FINAL1.html: knit file showing EDA, data visualization and analysis.<br /> 
preprocessed.csv: preprocessed and cleaned dataset used for EDA and statistical model.<br /> 
preprocessed_wosq.csv: preprocessed and cleaned dataset exclusing the columns with squared value attributes used for EDA and statistical model.<br /> 
Upsampling Minority Classes.ipynb: Script to implemenet upsampling and testing on a sample model for training(DT).<br /> 
Sample_testing_model_phase1.ipynb : python notebook consisting of basic statistical models for prediction and classification of Target variables along with analysis of scores and results of model.<br /> 
Sample_testing_model_phase2.ipynb : an addition to the previous version by implemeneting Random Forest Classifier, handling imbalance in the dataset(upsampling), implementing PCA( using function created in PCA/PCA_analysis ).Comparing the results.<br /> 
ModelBehaviour_LiteratureSurveyReport.pdf: Literature survey report of the project (Phase 1)<br /> 
ColumnMappings.txt: Detailed description of attributes of original train dataset along with the values it can take<br /> <br /> 

Link to our blog for updates:  https://modelbehaviour2019.blogspot.com/

### Reference
https://www.kaggle.com/c/costa-rican-household-poverty-prediction/overview







