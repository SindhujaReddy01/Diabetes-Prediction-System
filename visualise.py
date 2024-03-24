import warnings
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import tree
import streamlit as st



from web_functions import train_model

def app(df, X, y):
 
    

    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)


    st.title("Visualise the Diabetes Prediction Web app")


    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize = (10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)   
        bottom, top = ax.get_ylim()                            
        ax.set_ylim(bottom + 0.5, top - 0.5)                    
        st.pyplot(fig)

    if st.checkbox("Fasting Glucose Level vs Blood Pressure Plot"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="FastingGlc",y="BloodPressure",data=df)
        st.pyplot()

    if st.checkbox("Aftermeal Glucose Level vs Blood Pressure Plot"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="AfterGlc",y="BloodPressure",data=df)
        st.pyplot()

    if st.checkbox("Blood Pressure Level vs Skin Thickness Plot"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="BloodPressure",y="SkinThickness",data=df)
        st.pyplot()

    if st.checkbox("Show Histogram"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.histplot(data=df,x="Age",y="BloodPressure")
        st.pyplot()

    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(X, y)
      
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
            feature_names=X.columns, class_names=['0', '1']
        )
        st.graphviz_chart(dot_data)

